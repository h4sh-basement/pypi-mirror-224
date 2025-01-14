import construct #see docu at https://construct.readthedocs.io/en/latest/intro.html


FAR_payload = construct.Struct("CPU_TYPE" / construct.Byte,
                               "STDF_VER" / construct.Const(b"\x04"))

MIR_payload = construct.Struct("SETUP_T"  / construct.Int32ul                              * "Date and time of job setup",
                               "START_T"  / construct.Int32ul                              * "Date and time first part tested",
                               "STAT_NUM" / construct.Byte                                 * "Tester station number",
                               "MODE_COD" / construct.Byte                                 * "Test mode code (e.g. prod, dev) space",
                               "RTST_COD" / construct.Byte                                 * "Lot retest code space",
                               "PROT_COD" / construct.Byte                                 * "Data protection code space",
                               "BURN_TIM" / construct.Int16ul                              * "Burn-in time (in minutes) 65,535",
                               "CMOD_COD" / construct.Byte                                 * "Command mode code space",
                               "LOT_ID"   / construct.PascalString(construct.Byte, "ascii") * "Lot ID (customer specified)",
                               "PART_TYP" / construct.PascalString(construct.Byte, "ascii") * "Part Type (or product ID)",
                               "NODE_NAM" / construct.PascalString(construct.Byte, "ascii") * "Name of node that generated data",
                               "TSTR_TYP" / construct.PascalString(construct.Byte, "ascii") * "Tester type",
                               "JOB_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Job name (test program name)",
                               "JOB_REV"  / construct.PascalString(construct.Byte, "ascii") * "Job (test program) revision number length byte = 0",
                               "SBLOT_ID" / construct.PascalString(construct.Byte, "ascii") * "Sublot ID length byte = 0",
                               "OPER_NAM" / construct.PascalString(construct.Byte, "ascii") * "Operator name or ID (at setup time) length byte = 0",
                               "EXEC_TYP" / construct.PascalString(construct.Byte, "ascii") * "Tester executive software type length byte = 0",
                               "EXEC_VER" / construct.PascalString(construct.Byte, "ascii") * "Tester exec software version number length byte = 0",
                               "TEST_COD" / construct.PascalString(construct.Byte, "ascii") * "Test phase or step code length byte = 0",
                               "TST_TEMP" / construct.PascalString(construct.Byte, "ascii") * "Test temperature length byte = 0",
                               "USER_TXT" / construct.PascalString(construct.Byte, "ascii") * "Generic user text length byte = 0",
                               "AUX_FILE" / construct.PascalString(construct.Byte, "ascii") * "Name of auxiliary data file length byte = 0",
                               "PKG_TYP"  / construct.PascalString(construct.Byte, "ascii") * "Package type length byte = 0",
                               "FAMLY_ID" / construct.PascalString(construct.Byte, "ascii") * "Product family ID length byte = 0",
                               "DATE_COD" / construct.PascalString(construct.Byte, "ascii") * "Date code length byte = 0",
                               "FACIL_ID" / construct.PascalString(construct.Byte, "ascii") * "Test facility ID length byte = 0",
                               "FLOOR_ID" / construct.PascalString(construct.Byte, "ascii") * "Test floor ID length byte = 0",
                               "PROC_ID"  / construct.PascalString(construct.Byte, "ascii") * "Fabrication process ID length byte = 0",
                               "OPER_FRQ" / construct.PascalString(construct.Byte, "ascii") * "Operation frequency or step length byte = 0",
                               "SPEC_NAM" / construct.PascalString(construct.Byte, "ascii") * "Test specification name length byte = 0",
                               "SPEC_VER" / construct.PascalString(construct.Byte, "ascii") * "Test specification version number length byte = 0",
                               "FLOW_ID"  / construct.PascalString(construct.Byte, "ascii") * "Test flow ID length byte = 0",
                               "SETUP_ID" / construct.PascalString(construct.Byte, "ascii") * "Test setup ID length byte = 0",
                               "DSGN_REV" / construct.PascalString(construct.Byte, "ascii") * "Device design revision length byte = 0",
                               "ENG_ID"   / construct.PascalString(construct.Byte, "ascii") * "Engineering lot ID length byte = 0",
                               "ROM_COD"  / construct.PascalString(construct.Byte, "ascii") * "ROM code ID length byte = 0",
                               "SERL_NUM" / construct.PascalString(construct.Byte, "ascii") * "Tester serial number length byte = 0",
                               "SUPR_NAM" / construct.PascalString(construct.Byte, "ascii") * "Supervisor name or ID length byte = 0")

SDR_payload = construct.Struct("HEAD_NUM"  /     construct.Byte                                     *  "Test head number",
                               "SITE_GRP"  /     construct.Byte                                     *  "Site group number",
                               "SITE_CNT"  /     construct.Byte                                     *  "Number (k) of test sites in site group",
                               "SITE_NUM"  /     construct.Bytes(lambda this: this.SITE_CNT)        *  "Array of test site numbers",
                               "HAND_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Handler or prober type length byte = 0",
                               "HAND_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Handler or prober ID length byte = 0",
                               "CARD_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Probe card type length byte = 0",
                               "CARD_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Probe card ID length byte = 0",
                               "LOAD_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Load board type length byte = 0",
                               "LOAD_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Load board ID length byte = 0",
                               "DIB_TYP"   /     construct.PascalString(construct.Byte, "ascii")     *  "DIB board type length byte = 0",
                               "DIB_ID"    /     construct.PascalString(construct.Byte, "ascii")     *  "DIB board ID length byte = 0",
                               "CABL_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Interface cable type length byte = 0",
                               "CABL_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Interface cable ID length byte = 0",
                               "CONT_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Handler contactor type length byte = 0",
                               "CONT_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Handler contactor ID length byte = 0",
                               "LASR_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Laser type length byte = 0",
                               "LASR_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Laser ID length byte = 0",
                               "EXTR_TYP"  /     construct.PascalString(construct.Byte, "ascii")     *  "Extra equipment type field length byte = 0",
                               "EXTR_ID"   /     construct.PascalString(construct.Byte, "ascii")     *  "Extra equipment ID length byte = 0")

PMR_payload = construct.Struct("PMR_INDX"  /  construct.Int16ul                                                 * "Unique index associated with pin",
                               "CHAN_TYP"  /  construct.Int16ul                                                 * "Channel type 0",
                               "CHAN_NAM"  /  construct.PascalString(construct.Byte, "ascii")                    * "Channel name length byte = 0",
                               "PHY_NAM"   /  construct.PascalString(construct.Byte, "ascii")                    * "Physical name of pin length byte = 0",
                               "LOG_NAM"   /  construct.PascalString(construct.Byte, "ascii")                    * "Logical name of pin length byte = 0",
                               "HEAD_NUM"  /  construct.Byte                                                    * "Head number associated with channel 1",
                               "SITE_NUM"  /  construct.Byte                                                    * "Site number associated with channel 1")

PGR_payload = construct.Struct("GRP_INDX" /      construct.Int16ul                                              *  "Unique index associated with pin group",
                               "GRP_NAM"  /      construct.PascalString(construct.Byte, "ascii")                 *  "Name of pin group length byte = 0",
                               "INDX_CNT" /      construct.Int16ul                                              *  "Count (k) of PMR indexes",
                               "PMR_INDX" /      construct.Array(lambda this: this.INDX_CNT, construct.Int16ul) *  "Array of indexes for pins in the group INDX_CNT = 0)")

WCR_payload = construct.Struct("WAFR_SIZ"   / construct.Float32l              * "Diameter of wafer in WF_UNITS 0",
                               "DIE_HT"     / construct.Float32l              * "Height of die in WF_UNITS 0",
                               "DIE_WID"    / construct.Float32l              * "Width of die in WF_UNITS 0",
                               "WF_UNITS"   / construct.Int8ul                * "Units for wafer and die dimensions 0",
                               "WF_FLAT"    / construct.Byte                  * "Orientation of wafer flat space",
                               "CENTER_X"   / construct.Int16sl               * "X coordinate of center die on wafer -32768",
                               "CENTER_Y"   / construct.Int16sl               * "Y coordinate of center die on wafer -32768",
                               "POS_X"      / construct.Byte                  * "Positive X direction of wafer space",
                               "POS_Y"      / construct.Byte                  * "Positive Y direction of wafer space")


def decider(this, bits2check):
    try:
        return bool((int(this.OPT_FLAG) & bits2check) == 0)
    except:
        return False
    

PTR_payload = construct.Struct("TEST_NUM"  /   construct.Int32ul                                                                               * "Test number",
                               "HEAD_NUM"  /   construct.Byte                                                                                  * "Test head number",
                               "SITE_NUM"  /   construct.Byte                                                                                  * "Test site number",
                               "TEST_FLG"  /   construct.Byte                                                                                  * "Test flags (fail, alarm, etc.)",
                               "PARM_FLG"  /   construct.Byte                                                                                  * "Parametric test flags (drift, etc.)",
                               "RESULT"    /   construct.Float32l                                                                              * "Test result TEST_FLG bit 1 = 1",
                               "TEST_TXT"  /   construct.PascalString(construct.Byte, "ascii")                                                 * "Test description text or label length byte = 0",
                               "ALARM_ID"  /   construct.PascalString(construct.Byte, "ascii")                                                 * "Name of alarm length byte = 0",
                               "OPT_FLAG"  /   construct.Optional(construct.Byte)                                                              * "Optional data flag See note",
                               "RES_SCAL"  /   construct.Optional(construct.Int8sl)                                                            * "Test results scaling exponent OPT_FLAG bit 0 = 1",
                               "LLM_SCAL"  /   construct.Optional(construct.If(lambda this: decider(this, 0x50), construct.Int8sl))    * "Low limit scaling exponent OPT_FLAG bit 4 or 6 = 1",
                               "HLM_SCAL"  /   construct.Optional(construct.If(lambda this: decider(this, 0xA0), construct.Int8sl))    * "High limit scaling exponent OPT_FLAG bit 5 or 7 = 1",
                               "LO_LIMIT"  /   construct.Optional(construct.If(lambda this: decider(this, 0x50), construct.Float32l))  * "Low test limit value OPT_FLAG bit 4 or 6 = 1",
                               "HI_LIMIT"  /   construct.Optional(construct.If(lambda this: decider(this, 0xA0), construct.Float32l))  * "High test limit value OPT_FLAG bit 5 or 7 = 1",
                               "UNITS"     /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "Test units length byte = 0",
                               "C_RESFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C result format string length byte = 0",
                               "C_LLMFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C low limit format string length byte = 0",
                               "C_HLMFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C high limit format string length byte = 0",
                               "LO_SPEC"   /   construct.Optional(construct.If(lambda this: decider(this, 0x04), construct.Float32l))           * "Low specification limit value OPT_FLAG bit 2 = 1",
                               "HI_SPEC"   /   construct.Optional(construct.If(lambda this: decider(this, 0x08), construct.Float32l))           * "High specification limit value OPT_FLAG bit 3 = 1")

SBR_payload = construct.Struct("HEAD_NUM"  / construct.Int8ul                                * "Test head number See note",
                               "SITE_NUM"  / construct.Int8ul                                * "Test site number",
                               "SBIN_NUM"  / construct.Int16ul                               * "Software bin number",
                               "SBIN_CNT"  / construct.Int32ul                               * "Number of parts in bin",
                               "SBIN_PF"   / construct.Byte                                  * "Pass/fail indication space",
                               "SBIN_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Name of software bin length byte = 0")

HBR_payload = construct.Struct("HEAD_NUM"  / construct.Int8ul                                * "Test head number See note",
                               "SITE_NUM"  / construct.Int8ul                                * "Test site number",
                               "HBIN_NUM"  / construct.Int16ul                               * "Software bin number",
                               "HBIN_CNT"  / construct.Int32ul                               * "Number of parts in bin",
                               "HBIN_PF"   / construct.Byte                                  * "Pass/fail indication space",
                               "HBIN_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Name of software bin length byte = 0")

PCR_payload = construct.Struct("HEAD_NUM" / construct.Int8ul  * "Test head number See note",
                               "SITE_NUM" / construct.Int8ul  * "Test site number",
                               "PART_CNT" / construct.Int32ul * "Number of parts tested",
                               "RTST_CNT" / construct.Int32ul * "Number of parts retested 4,294,967,295",
                               "ABRT_CNT" / construct.Int32ul * "Number of aborts during testing 4,294,967,295",
                               "GOOD_CNT" / construct.Int32ul * "Number of good (passed) parts tested 4,294,967,295",
                               "FUNC_CNT" / construct.Int32ul * "Number of functional parts tested 4,294,967,295")

MRR_payload = construct.Struct("FINISH_T" / construct.Int32ul                              * "Date and time last part tested",
                               "DISP_COD" / construct.Byte                                 * "Lot disposition code space",
                               "USR_DESC" / construct.PascalString(construct.Byte, "ascii") * "Lot description supplied by user length byte = 0",
                               "EXC_DESC" / construct.PascalString(construct.Byte, "ascii") * "Lot description supplied by exec length byte = 0")

WIR_payload = construct.Struct("HEAD_NUM" / construct.Int8ul                               * "Test head number",
                               "SITE_GRP" / construct.Int8ul                               * "Site group number",
                               "START_T" / construct.Int32ul                               * "Lot description supplied by user length byte = 0",
                               "WAFER_ID" / construct.PascalString(construct.Byte, "ascii") * "Waver ID")

PIR_payload =  construct.Struct( "HEAD_NUM" / construct.Int8ul                              *  "Test head number",
                                 "SITE_NUM" / construct.Int8ul                              *  "Test site number")

PRR_payload =  construct.Struct( "HEAD_NUM" / construct.Int8ul                               *  "Test head number",
                                 "SITE_NUM" / construct.Int8ul                               *  "Test site number",
                                 "PART_FLG" / construct.Int8ul                               *  "Part information flag",
                                 "NUM_TEST" / construct.Int16ul                              *  "Number of tests executed",
                                 "HARD_BIN" / construct.Int16ul                              *  "Hardware bin number",
                                 "SOFT_BIN" / construct.Int16ul                              *  "Software bin number 65535",
                                 "X_COORD"  / construct.Int16sl                              * "(Wafer) X coordinate -32768",
                                 "Y_COORD"  / construct.Int16sl                              * "(Wafer) Y coordinate -32768",
                                 "TEST_T"   / construct.Int32ul                              * "Elapsed test time in milliseconds 0",
                                 "PART_ID"  / construct.PascalString(construct.Byte, "ascii") * "Part identification length byte = 0",
                                 "PART_TXT" / construct.PascalString(construct.Byte, "ascii") * "Part description text length byte = 0",
                                 "PART_FIX" / construct.PascalString(construct.Byte, "ascii") * "Part repair information length byte = 0")

TSR_payload =  construct.Struct("HEAD_NUM" / construct.Byte    *                            "Test head number See note",
                                "SITE_NUM" / construct.Byte    *                            "Test site number",
                                "TEST_TYP" / construct.Byte    *                            "Test type space",
                                "TEST_NUM" / construct.Int32ul *                            " Test number",
                                "EXEC_CNT" / construct.Int32ul *                            " Number of test executions 4,294,967,295",
                                "FAIL_CNT" / construct.Int32ul *                            " Number of test failures 4,294,967,295",
                                "ALRM_CNT" / construct.Int32ul *                            " Number of alarmed tests 4,294,967,295",
                                "TEST_NAM" / construct.PascalString(construct.Byte, "ascii") * "Test name length byte = 0",
                                "SEQ_NAME" / construct.PascalString(construct.Byte, "ascii") * "Sequencer (program segment/flow) name length byte = 0",
                                "TEST_LBL" / construct.PascalString(construct.Byte, "ascii") * "Test label or text length byte = 0",
                                "OPT_FLAG" / construct.Optional(construct.Byte)                                 * "Optional data flag See note",
                                "TEST_TIM" / construct.Optional(construct.If(lambda this: decider(this, 0x04),construct.Float32l))                             * " Average test execution time in seconds OPT_FLAG bit 2 = 1",
                                "TEST_MIN" / construct.Optional(construct.If(lambda this: decider(this, 0x01),construct.Float32l))                             * " Lowest test result value OPT_FLAG bit 0 = 1",
                                "TEST_MAX" / construct.Optional(construct.If(lambda this: decider(this, 0x02),construct.Float32l))                             * " Highest test result value OPT_FLAG bit 1 = 1",
                                "TST_SUMS" / construct.Optional(construct.If(lambda this: decider(this, 0x10),construct.Float32l))                             * " Sumof test result values OPT_FLAG bit 4 = 1",
                                "TST_SQRS" / construct.Optional(construct.If(lambda this: decider(this, 0x20),construct.Float32l))                             * " Sum of squares of test result values OPT_FLAG bit 5 = 1")

_dict_of_payloads = {#Required
                     tuple((0x00, 0x0a)): FAR_payload.compile(),
                     tuple((0x01, 0x0a)): MIR_payload.compile(),
                     tuple((5,10)):       PIR_payload.compile(),
                     tuple((15,10)):      PTR_payload.compile(),
                     tuple((0x05,0x14)):  PRR_payload.compile(),
                     tuple((1,20)):       MRR_payload.compile(),
                     #optional
                     tuple((2, 30)):      WCR_payload.compile(),
                     tuple((0x01, 0x50)): (SDR_payload),
                     tuple((0x01, 60)):   PMR_payload.compile(),
                     tuple((0x01, 62)):   (PGR_payload),
                     tuple((1,50)):       SBR_payload.compile(),
                     tuple((1,30)):       PCR_payload.compile(),
                     tuple((10,30)):      TSR_payload.compile(),
                     tuple((2,10)):       WIR_payload.compile(),
                     tuple((5,10)):       PIR_payload.compile(),
                     tuple((1,40)):       HBR_payload.compile()}

def calc_len_of_stdf_record(this):
    pl_construct = _dict_of_payloads[tuple((this.REC_TYP, this.REC_SUB))]
    return len(pl_construct.build(this.PL))

RECORD = construct.Struct("REC_LEN"  / construct.Rebuild(construct.Int16ul, calc_len_of_stdf_record) * "Bytes of data following header",
                          "REC_TYP"  / construct.Byte                                  * "Record type (1)",
                          "REC_SUB"  / construct.Byte                                  * "Record sub-type (10)",
                          "PL"       / construct.Switch(lambda this: tuple((this.REC_TYP, this.REC_SUB)), _dict_of_payloads))

def parse_record(stream):
    """ This function parses in 2 stages.

    Get header and raw payload, then parse deeply from just this record.
    This way the REC_LEN field is driving the advancing in the stream.
    """
    length = stream.read(2)
    if not length:
        raise EOFError()
    data = length + stream.read(((length[1]<<8)+length[0])+2)
    return RECORD.parse(data)

