## Cognitive Risk Assessment – Variable Mapping Documentation

This document explains each input variable used in the Streamlit application, including original dataset meaning, response coding, and the user-facing labels used in the interface.

---

## 1. cg13ofmemprob

**Original label:** R13 CG3 OFTN MEMRY PROBS INTERFER
**Meaning:** Frequency of memory problems interfering with daily life

| Value | Meaning                      | App Label |
| ----- | ---------------------------- | --------- |
| 1     | Every day                    | Every day |
| 2     | Most days (5–6 days/week)    | Most days |
| 3     | Some days (2–4 days/week)    | Some days |
| 4     | Rarely (once a week or less) | Rarely    |
| 5     | Never                        | Never     |

---

## 2. hh13dhshldnum

**Original label:** R13 D TOTAL NUMBER IN HOUSEHOLD
**Meaning:** Number of people living in the household

| Value | Meaning                     | App Label                    |
| ----- | --------------------------- | ---------------------------- |
| 1–12  | Number of household members | Same numeric value displayed |

---

## 3. rl13dracehisp

**Original label:** R13 D RACE AND HISPANIC ETHNICITY WHEN ADDED
**Meaning:** Race/ethnicity classification

| Value | Meaning                      | App Label                      |
| ----- | ---------------------------- | ------------------------------ |
| 1     | White, non-Hispanic          | White, non-Hispanic            |
| 2     | Black, non-Hispanic          | Black, non-Hispanic            |
| 3     | Other non-Hispanic           | Other, non-Hispanic            |
| 4     | Hispanic                     | Hispanic                       |
| 5     | More than one / DKRF primary | More than one                  |
| 6     | DKRF                         | Unknown / Prefer not to answer |

---

## 4. pc13up20stair

**Meaning:** Ability to walk up 20 stairs

| Value | Meaning | App Label |
| ----- | ------- | --------- |
| 1     | Yes     | Yes       |
| 2     | No      | No        |

---

## 5. pc13car20pnds

**Meaning:** Ability to carry 20 pounds

| Value | Meaning | App Label |
| ----- | ------- | --------- |
| 1     | Yes     | Yes       |
| 2     | No      | No        |

---

## 6. pc13bendover

**Meaning:** Ability to bend over

| Value | Meaning | App Label |
| ----- | ------- | --------- |
| 1     | Yes     | Yes       |
| 2     | No      | No        |

---

## 7. pc13hvobovrhd

**Meaning:** Ability to lift heavy objects overhead

| Value | Meaning | App Label |
| ----- | ------- | --------- |
| 1     | Yes     | Yes       |
| 2     | No      | No        |

---

## 8. cg13ratememry

**Meaning:** Self-rated memory quality

| Value | Meaning   | App Label |
| ----- | --------- | --------- |
| 1     | Excellent | Excellent |
| 2     | Very good | Very Good |
| 3     | Good      | Good      |
| 4     | Fair      | Fair      |
| 5     | Poor      | Poor      |

---

## 9. mo13outhlp

**Meaning:** Need help going outside

| Value | Meaning | App Label |
| ----- | ------- | --------- |
| 1     | Yes     | Yes       |
| 2     | No      | No        |

---

## 10. mo13beddev

**Meaning:** Use of assistive device when getting out of bed

| Value | Meaning    | App Label  |
| ----- | ---------- | ---------- |
| 1     | Every time | Every time |
| 2     | Most times | Most times |
| 3     | Sometimes  | Sometimes  |
| 4     | Rarely     | Rarely     |
| 5     | Never      | Never      |

---

## 11. wb13offelche1

**Meaning:** Frequency of feeling cheerful

| Value | Meaning   | App Label |
| ----- | --------- | --------- |
| 1     | Every day | Every day |
| 2     | Most days | Most days |
| 3     | Some days | Some days |
| 4     | Rarely    | Rarely    |
| 5     | Never     | Never     |

---

## 12. wb13truestme3

**Meaning:** “I gave up improving my life”

| Value | Meaning        | App Label        |
| ----- | -------------- | ---------------- |
| 1     | Agree a lot    | Agree a lot      |
| 2     | Agree a little | Agree a little   |
| 3     | Not at all     | Agree not at all |

---

## 13. wb13agrwstmt1

**Meaning:** Self-determination (“I am able to make my own decisions”)

| Value | Meaning          | App Label        |
| ----- | ---------------- | ---------------- |
| 1     | Agree a lot      | Agree a lot      |
| 2     | Agree a little   | Agree a little   |
| 3     | Agree not at all | Agree not at all |

---

## Notes on Encoding

* All variables retain original numeric encoding for model compatibility
* Missing codes (e.g., -1, -9, DKRF categories) were removed from user input
* User interface displays only human-readable labels
* Internal model prediction uses original trained feature structure
