// The class for the Candid Type: opt

#include "candid_type.h"
#include "candid_type_opt_nat64.h"
#include "candid_assert.h"
#include "candid_opcode.h"

#include <cassert>

#include "icpp_hooks.h"

CandidTypeOptNat64::CandidTypeOptNat64() : CandidTypeOptBase() {
  std::optional<uint64_t> v;
  set_v(v);
  initialize();
}

// These constructors allows for setting the value during Deserialization
CandidTypeOptNat64::CandidTypeOptNat64(std::optional<uint64_t> *p_v)
    : CandidTypeOptBase() {
  set_pv(p_v);

  const std::optional<uint64_t> v = const_cast<std::optional<uint64_t> &>(*p_v);
  set_v(v);
  initialize();
}

// These constructors are only for encoding
CandidTypeOptNat64::CandidTypeOptNat64(const std::optional<uint64_t> v)
    : CandidTypeOptBase() {
  set_v(v);
  initialize();
}

CandidTypeOptNat64::~CandidTypeOptNat64() {}

void CandidTypeOptNat64::set_content_type() {
  m_content_type_opcode = CandidOpcode().Nat64;
  m_content_type_hex = OpcodeHex().Nat64;
  m_content_type_textual = OpcodeTextual().Nat64;
}

void CandidTypeOptNat64::encode_M() {
  // https://github.com/dfinity/candid/blob/master/spec/Candid.md#memory
  // M(null : opt <datatype>) = i8(0)
  // M(?v   : opt <datatype>) = i8(1) M(v : <datatype>)

  if (!m_v.has_value()) {
    m_M.append_int_fixed_width(uint8_t{0});
  } else {
    m_M.append_int_fixed_width(uint8_t{1});
    m_M.append_int_fixed_width(m_v.value());
  }
}

// Decode the values, starting at & updating offset
bool CandidTypeOptNat64::decode_M(VecBytes B, __uint128_t &offset,
                                  std::string &parse_error) {
  // https://github.com/dfinity/candid/blob/master/spec/Candid.md#memory
  // M(null : opt <datatype>) = i8(0)
  // M(?v   : opt <datatype>) = i8(1) M(v : <datatype>)

  // get tag of opt - i8(0)
  // this will also work if there is a null on the wire.
  __uint128_t offset_start = offset;
  parse_error = "";
  uint8_t tag;
  if (B.parse_int_fixed_width(offset, tag, parse_error)) {
    std::string to_be_parsed = "Opt tag.";
    CandidAssert::trap_with_parse_error(offset_start, offset, to_be_parsed,
                                             parse_error);
  }
  if (tag == 1) {
    uint64_t v;
    offset_start = offset;
    parse_error = "";
    if (B.parse_int_fixed_width(offset, v, parse_error)) {
      std::string to_be_parsed = "Opt: Value for CandidTypeNat64";
      CandidAssert::trap_with_parse_error(offset_start, offset,
                                               to_be_parsed, parse_error);
    }
    m_v = v;

  } else if (tag != 0) {
    ICPP_HOOKS::trap("ERROR: tag in opt nat64 coming from wire is not 0 or 1");
  }

  // Fill the user's data placeholder, if a pointer was provided
  if (m_pv) *m_pv = m_v;

  return false;
}