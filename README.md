# JSON Parser

- This is a weekend project that I made based on this template: [Coding Challenges - JSON Parser](https://codingchallenges.fyi/challenges/challenge-json-parser)

## Relevant Links

- [RFC 8259 - Actual JSON specification](https://www.rfc-editor.org/info/std90)
- [Visual JSON specification from JSON.org](https://www.json.org/json-en.html)

## Checklist

### Step 0

- [X] Create repository
- [X] Download dependencies for testing, linting, etc
- [X] Download JSON test data from [here](https://www.dropbox.com/s/vthtr4897fkuhw8/tests.zip?dl=0)

### Step 1

- [X] `{}` should be a valid JSON
- [X] empty string should not be a valid JSON
- [X] `{` or `}` should not be a valid JSON
- [X] Implement parsing a file

### Step 2

- [ ] Parse a simple JSON object with string keys and string values

- A **string** is a sequence of N characters wrapped in single or double quotes
  - For simplicity, strings cannot be empty (`""`)
    - All opening quotes should be closed (total number of quotes must be even or 0)
- All keys need to have a value
- Keys and values should be separated by a `:` colon
- An **attribute** is the combined unit of a key and a value
  - If an object has more than one attribute, they should be separated by commas

(I'll be putting more steps here as I go along)
