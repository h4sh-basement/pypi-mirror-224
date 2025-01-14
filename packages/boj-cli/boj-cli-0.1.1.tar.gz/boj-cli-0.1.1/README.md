# boj-cli

백준 온라인 저지 커맨드라인 인터페이스  
<img src="https://github.com/xvzc/boj-cli/assets/45588457/f6fcf5b8-b5bd-4674-b018-c6574e98b1c4" width="65%" height="65%">

# 설치
`$ pip install boj-cli`

# 로컬 설정
`default_language`에 들어갈 수 있는 값들은 [지원 언어](#지원-언어)를 참고해주세요.
> ~/.boj-cli/config.json
```
{
    "filetype": {
        "py": {
            "default_language": "python3",
            "run": "python3 $file"
        },
        "cpp": {
            "default_language": "c++17",
            "compile": "g++ -std=c++17 -O2 -Wall -Wno-sign-compare $file -o a.out",
            "run": "./a.out"
        }
    }
}
```

# 사용법

## 로그인
백준 온라인 저지에서는 로그인 시 `reCAPTCHA`를 사용하고있기 때문에 로그인 과정은 조금 번거로울 수 있습니다. 
```
$ boj login
```
위 명령어를 실행하면 `selenium` 브라우저가 실행됩니다. 로그인 정보를 입력하고 `reCAPTCHA`를 수행하면 로그인 세션 정보는 암호화되어 저장됩니다.
> 로그인 시 "로그인 상태 유지" 체크 박스를 반드시 선택해주세요.

---

## 테스트케이스 불러오기
백준 온라인저지에 올라와있는 문제에서 테스트케이스를 추려내어 현재 경로에 `testcase.yaml` 파일을 생성합니다.
생성된 `testcase.yaml`의 포멧에 맞게 커스텀 테스트케이스 또한 추가할 수 있습니다.
```
$ boj init 1000
```

---

## 테스트케이스 실행하기
`init` 명령어로 생성한 테스트케이스를 활용해 `testcase.yaml` 파일에 있는 모든 테스트케이스를 비동기적으로 실행하고
정답을 비교합니다.

```
$ boj run {FILE_PATH}
```

### Options
```
--verbose : 자세한 아웃풋을 출력합니다. (예: 컴파일 에러)  
--timeout int(sec): 각 테스트케이스의 타임아웃을 설정합니다 (Default: 5초)
```

---

## 코드 제출하기
로컬 소스 파일을 백준 온라인 저지에 제출하고 채점 현황을 실시간으로 출력합니다.
```
$ boj submit {FILE_PATH}
```

### Options
```
--lang: 제출할 언어를 선택합니다. 옵션이 주어지지 않은경우 local configuration 값으로 실행됩니다.
```
> lang 옵션으로 설정할 수 있는 값은 [여기](https://github.com/xvzc/boj-cli/blob/main/boj/core/__init__.py#L12)에서 **LANGUAGE_DICT** 변수의 키값들을 확인해주세요.  
 
> 매번 인자를 넣지 않아도 파일타입에 따른 기본 언어 설정을 할 수 있습니다.
> [예제](https://github.com/xvzc/boj-cli/blob/main/config_example.json)를 참고해주세요.  
> 설정 파일의 위치는 `~/.boj-cli/config.json` 입니다. 파일을 생성해주세요.

---

## 브라우저에서 문제 링크 열기
문제 링크를 기본 브라우저에서 엽니다.
```
$ boj problem {problem_id}
ex) boj problem 1234
```

---

## 랜덤 문제 브라우저에서 열기
랜덤 문제 링크를 기본 브라우저에서 엽니다.
```
$ boj random {tier} --{level}
ex) boj random bronze --easy
```

### Options
```
--easy: 5티어 문제만
--normal: 3 ~ 4티어 문제
--hard: 1 ~ 2티어 문제
```
> level 옵션을 주지 않으면 해당 티어의 1~5 단계 문제중 랜덤으로 선택됩니다.  
> '내가 풀지 않은 문제' 만 쿼리됩니다.

# 지원 언어
- `c++17`
- `python3`
- `pypy3`
- `c11`
- `text`
- `golfscript`
- `java8`
- `c++98`
- `ruby`
- `c99`
- `c++11`
- `java11`
- `kotlin(jvm)`
- `c++14`
- `swift`
- `java8(openjdk)`
- `c++20`
- `c#`
- `node.js`
- `go`
- `d`
- `rust2018`
- `go(gccgo)`
- `c++17(clang)`
- `java15`
- `d(ldc)`
- `php`
- `rust2015`
- `pascal`
- `lua`
- `perl`
- `f#`
- `visual-basic`
- `objective-c`
- `objective-c++`
- `c99(clang)`
- `c++98(clang)`
- `c++11(clang)`
- `c++14(clang)`
- `c11(clang)`
- `c++20(clang)`
- `c90`
- `c2x`
- `c90(clang)`
- `c2x(clang)`
- `typescript`
- `assembly(32bit)`
- `assembly(64bit)`
- `bash`
- `fortran`
- `scheme`
- `ada`
- `awk`
- `o-caml`
- `brainf**k`
- `whitespace`
- `tcl`
- `rhino`
- `cobol`
- `pike`
- `sed`
- `intercal`
- `bc`
- `algol68`
- `befunge`
- `free-basic`
- `haxe`
- `lolcode`
- `아희`
- `system-verilog`
- `rust2021`
- `scala`

