# SmartIR Code Analysis

This document details issues found in SmartIR climate device code files that require re-recording of IR codes.

## 1003.json - Mitsubishi Electric SRK25ZSX-SRC25ZSX

**File**: `./custom_components/smartir/codes/climate/1003.json`

**Expected Codes**: 261 total codes
- Modes: cool, heat, dry, fan_only
- Fan speeds: auto, low, mid, high
- Temperature range: 16-30°C (15 steps)

### Issues Found

#### 1. heat/mid/19 - Corrupted Code
- **Status**: Corrupted
- **Current Code**: Starts with `JgD` (invalid prefix)
- **Length**: 320 characters (expected ~420)
- **Action Required**: Re-record IR code for Heat mode, Mid fan speed, 19°C

#### 2. heat/low/19 - Suspicious Code
- **Status**: Suspicious
- **Current Code**: Starts with `JgAm` (unusual prefix)
- **Length**: 400 characters (expected ~420)
- **Action Required**: Verify and potentially re-record IR code for Heat mode, Low fan speed, 19°C

### Summary
- **Total Issues**: 2 codes need attention
- **JSON Validity**: Valid
- **Structure**: Correct
- **Note**: Dry mode correctly uses same codes for all fan speeds (expected behavior)

---

## 1002.json - Panasonic CS-Z25TK

**File**: `./custom_components/smartir/codes/climate/1002.json`

**Expected Codes**: 346 total codes
- Modes: cool, heat, dry, fan_only
- Fan speeds: auto, low, mid, high, highest, lowest
- Temperature range: 16-30°C (15 steps)

### Issues Found

#### 1. fan_only/auto - Missing Code
- **Status**: Missing entirely
- **Action Required**: Record IR code for Fan Only mode, Auto fan speed

#### 2. heat/lowest/16 - Unexpected Prefix
- **Status**: Suspicious
- **Current Code**: Starts with `JgBKA` (unusual prefix, expected `JgA`)
- **Length**: 440 characters (within expected range)
- **Action Required**: Verify IR code for Heat mode, Lowest fan speed, 16°C

#### 3. dry/auto/26 - Unexpected Prefix
- **Status**: Suspicious
- **Current Code**: Starts with `JgDAA` (unusual prefix, expected `JgA`)
- **Length**: 420 characters (within expected range)
- **Action Required**: Verify IR code for Dry mode, Auto fan speed, 26°C

### Summary
- **Total Issues**: 3 codes need attention (1 missing, 2 suspicious)
- **JSON Validity**: Valid
- **Structure**: Mostly correct (missing one code)
- **Note**: Fan_only mode correctly uses same codes for all temperatures (expected behavior)

---

## Analysis Methodology

IR codes in SmartIR are Base64-encoded Broadlink device codes. Typical characteristics:

1. **Valid Prefixes**: Most codes start with `JgA` followed by additional characters
2. **Length**: Codes typically range from 380-440 characters
3. **Structure**: Each mode/fan/temperature combination should have a unique code
4. **Exceptions**: Some modes (dry, fan_only) may reuse codes across certain dimensions

### Detection Criteria

Codes were flagged as problematic if they exhibited:
- Unusual prefixes (not starting with `JgA`)
- Significantly shorter length than expected
- Missing entries in expected mode/fan/temperature combinations

---

## Recommendations

1. **Priority 1 - Missing Code**: Record `fan_only/auto` for 1002.json
2. **Priority 2 - Corrupted Code**: Re-record `heat/mid/19` for 1003.json
3. **Priority 3 - Verification**: Test and verify the 3 codes with suspicious prefixes:
   - 1003.json: `heat/low/19`
   - 1002.json: `heat/lowest/16`, `dry/auto/26`

## Impact

These issues may cause:
- Commands not being sent to the AC unit
- Incorrect settings being applied
- Specific mode/fan/temperature combinations not working

Users should test these specific combinations and re-record IR codes as needed using the SmartIR IR code recording tools.
