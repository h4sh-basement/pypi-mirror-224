// Candid serialization class
// https://github.com/dfinity/candid/blob/master/spec/Candid.md#parameters-and-results

#include <variant>

#include "candid_type.h"
#include "candid_type_all_includes.h"
#include "candid_serialize.h"
#include "candid_assert.h"

// Default constructor handles nullary input '()'
CandidSerialize::CandidSerialize() { serialize(); }
CandidSerialize::CandidSerialize(const CandidType &a) {
  m_A.append(a);
  serialize();
}
CandidSerialize::CandidSerialize(const CandidArgs &A) : m_A{A} {
  serialize();
}

CandidSerialize::~CandidSerialize() {}

void CandidSerialize::serialize() {
  // https://github.com/dfinity/candid/blob/master/spec/Candid.md#parameters-and-results
  // B(kv* : <datatype>*) =
  // i8('D') i8('I') i8('D') i8('L')      magic number
  // T*(<comptype>*)                      type definition table
  // I*(<datatype>*)                      types of the argument list
  // M(kv* : <datatype>*)                 values of argument list

  m_B.clear();
  m_num_typetables = 0;
  m_type_table_A_index.clear();
  m_type_table_index.clear();
  // -------------------------------------------------------------------------------------
  // i8('D') i8('I') i8('D') i8('L')      magic number
  m_B.append_didl();

  // -------------------------------------------------------------------------------------
  // T*(<comptype>*)                      type definition table
  // Write the unique TypeTables of the comptypes:
  // (-) Constructed Types (opt, vec, record, variant)
  // (-) Reference Types (func, service)

  // Check how many unique typetables we have and set the index
  const __uint128_t NO_TYPE_TABLE = -9999999999999999;
  __uint128_t typetable_i = 0;

  for (size_t i = 0; i < m_A.m_args_ptrs.size(); ++i) {
    m_type_table_A_index.push_back(NO_TYPE_TABLE);
    m_type_table_index.push_back(NO_TYPE_TABLE);
    VecBytes T = m_A.m_args_ptrs[i]->get_T();

    if (T.size() > 0) {
      bool new_type_table = true;
      for (size_t i1 = 0; i1 < i; ++i1) {
        VecBytes T1 = m_A.m_args_ptrs[i1]->get_T();
        if (T == T1) {
          m_type_table_A_index[i] = m_type_table_A_index[i1];
          m_type_table_index[i] = m_type_table_index[i1];
          new_type_table = false;
          break;
        }
      }
      if (new_type_table) {
        m_type_table_A_index[i] = i;
        m_type_table_index[i] = m_num_typetables;
        ++m_num_typetables;
      }
    }
  }

  // Append the number of unique type tables
  m_B.append_uleb128(m_num_typetables);

  // Now write the unique type tables
  for (size_t i = 0; i < m_A.m_args_ptrs.size(); ++i) {
    if (m_type_table_A_index[i] == i) {
      VecBytes T = m_A.m_args_ptrs[i]->get_T();
      for (std::byte b : T.vec()) {
        m_B.append_byte(b);
      }
    }
  }

  // -------------------------------------------------------------------------------------
  // I*(<datatype>*)                      types of the argument list
  m_B.append_uleb128(__uint128_t(m_A.m_args_ptrs.size()));

  for (size_t i = 0; i < m_A.m_args_ptrs.size(); ++i) {
    VecBytes T = m_A.m_args_ptrs[i]->get_T();
    if (T.size() > 0) {
      // For <comptypes>, we use the index into the type table we defined above
      m_B.append_uleb128(m_type_table_index[i]);
    } else {
      // For <primtypes>, use the Opcode, already stored
      VecBytes I = m_A.m_args_ptrs[i]->get_I();
      for (std::byte b : I.vec()) {
        m_B.append_byte(b);
      }
    }
  }

  // -------------------------------------------------------------------------------------
  // M(kv* : <datatype>*)                 values of argument list
  for (std::shared_ptr<CandidTypeBase> p_c : m_A.m_args_ptrs) {
    VecBytes M = p_c->get_M();
    for (std::byte b : M.vec()) {
      m_B.append_byte(b);
    }
  }

  // Append R
  // Was never implemented in Candid, although it is still in the spec
  // https://www.joachim-breitner.de/blog/786-A_Candid_explainer__Quirks
}

// Assert the serialized candid VecBytes against a string in "hex" format (didc encode)
int CandidSerialize::assert_candid(const std::string &candid_expected,
                                   const bool &assert_value) {
  return CandidAssert::assert_candid(m_B, candid_expected, assert_value);
}
