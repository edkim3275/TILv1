# TypeScript

## 코드 편집기 설정

- 초기 편집기 설정

  - 새 디렉터리 생성

  ```
  mkdir directory-name
  cd directory-name
  ```

  - 새 NPM 프로젝트 초기화(프롬프트의 지시에 따름)

  ```
  npm init
  ```

  `package.json`을 만들기 위해서 `npm init`이라는 명령어를 사용.

  보통 `npm init`을 입력하면 npm project에 대한 기본 양식을 일일이 정해줘야 하는데 `-y` 속성을 이용하면 default값으로 설정된 package.json을 만들겠다는 의미.

  - TSC, TSLint, NodeJS용 타입 선언 설치

  ```
  npm install --save-dev typescript tslint @types/node
  ```

- **tsconfig.json**

  ```json
  {
      "compilerOptions": {
          "lib": ["es2015"],
          "module": "commonjs",
          "outDir": "dist",
          "sourceMap": true,
          "strict": true,
          "target": "es2015"
      },
      "include": [
          "src"
      ]
  }
  ```

  | 옵션      | 설명                                                         |
  | --------- | ------------------------------------------------------------ |
  | `include` | TSC가 타입스크립트 파일을 찾을 디렉터리                      |
  | `lib`     | TSC가 코드 실행 환경에서 이용할 수 있다고 가정하는 API       |
  | `module`  | TSC가 코드를 컴파일할 대상 모듈 시스템(CommonJS, SystemJS, ES2015 등) |
  | `outDir`  | 생성된 자바스크립트 코드를 출력할 디렉터리                   |
  | `strict`  | 유효하지 않은 코드를 확인할 때 가능한 한 엄격하게 검사. 이 옵션을 이용하면 코드가 적절하게 타입을 갖추도록 강제할 수 있다. |
  | `target`  | TSC가 코드를 컴파일할 자바스크립트 버전(ES3, ES5, ES2015, ES2016 등) |

  tsconfig.json이 지원하는 일부 옵션들이고, 모든 최신 옵션은 [타입스크립트 웹사이트](http://bit.ly/2JWfsgY)에서 확인.

- **tslint.json**

  탭을 사용할지 공백을 사용할지 등을 결정하는 코딩 스타일 규약. TSLint는 선택 사항이지만 모든 타입스크립트 프로젝트에 TSLint를 이용해 일관된 스타일을 사용하도록 강력히 권장한다.

  기본값으로 채워진 tslint.json 파일을 만드는 명령

  ```
  ./node_modules/.bin/tslint -init
  ```

  그리고 만들어진 파일을 자신의 코딩 스타일에 맞게 편집할 수 있다.

  ```json
  {
      "defaultSeverity": "error",
      "extends": [
          "tslint:recommended"
      ],
      "rules": {
          "semicolon": false,
          "trailing-comma": false
      }
  }
  ```

  rules에 지정 가능한 모든 규칙은 [TSLint 문서](https://palantir.github.io/tslint/rules/)에서 확인. 자신만의 규칙을 추가하거나 ReactJS용 TSLint처럼 미리 정해진 규칙을 추가로 설치할 수 있다.

- **index.ts**

`src` 디렉터리에 첫 번째 타입스크립트 파일을 추가

- 타입스크립트 코드를 컴파일하고 실행

  -  TSC로 타입스크립트 컴파일

    ```
    ./node_modules/.bin/tsc

  - NodeJS로 코드 실행

    ```
    node ./dist/index.js

## 타입

**타입(type)** : 값과 이 값으로 할 수 있는 일(연산, 메서드)의 집합

### 타입스크립트의 타입

각 타입이 무엇을 포함할 수 있는지, 어떤 동작을 수행할 수 있는지를 살펴보자. 타입 별칭(type alias), 유니온 타입(union type), 인터섹션 타입(intersection type) 등 여러 가지 언어 기능도 확인한다.

- **any**

