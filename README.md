# G4Starter

**G4Starter**는 Geant4 시뮬레이션 코드를 작성하는 어려움을 덜어드리기 위해 만들어진 도구입니다.
프로그래밍 지식이 없어도, 화면에 나오는 질문에 **화살표 키로 답변만 선택하면** 바로 컴파일 가능한 Geant4 C++ 프로젝트 초안을 만들어줍니다.

## ✨ 주요 특징

* **설치 불필요:** Python이나 추가 라이브러리를 설치할 필요가 없습니다. (실행 파일만 있으면 OK)
* **직관적인 인터페이스:** 복잡한 명령어 대신 간단한 입력과 엔터(Enter)만 사용합니다.
* **자동 코드 생성:** `CMakeLists.txt`, `main.cc`, 그리고 필수 클래스 파일들을 자동으로 생성합니다.
* **멀티 플랫폼:** Windows, macOS, Linux 어디서든 실행 가능합니다.

---

## 📥 다운로드 및 실행 방법

### 1. 프로그램 다운로드
이 저장소의 **[Releases]** 페이지에서 운영체제에 맞는 파일을 다운로드하세요.

* **Windows:** `G4Starter.exe`
* **macOS:** `G4Starter_mac`
* **Linux:** `G4Starter_linux`

### 2. 실행하기
다운로드한 파일을 더블 클릭하거나 터미널에서 실행합니다.
(macOS/Linux의 경우 처음에 권한 설정이 필요할 수 있습니다: `chmod +x G4Starter_xxx`)

### 3. 옵션 선택
화면에 나오는 질문에 따라 시뮬레이션 환경을 설정합니다.
* 물질 선택 (Air, Water 등)
* 도형 모양 및 크기 설정
* 입자 종류 및 에너지 설정
* 기타 설정

### 4. 결과 확인
프로그램이 종료되면, 실행한 위치에 **새로운 폴더**가 생성됩니다. 해당 폴더 안에 Geant4 C++ 코드가 들어있습니다.

---

## 🛠 생성되는 프로젝트 구조

G4Starter를 통해 생성된 폴더는 기본적인 Geant4 구조를 갖추고 있으며, 선택한 옵션에 따라 파일이 추가될 수 있습니다.

```
MyGeant4Project/
├── CMakeLists.txt       # 빌드 설정 파일
├── main.cc              # 메인 프로그램
├── include/             # 헤더 파일 (.hh)
│   ├── DetectorConstruction.hh
│   ├── PrimaryGeneratorAction.hh
│   └── ...              # 기타 헤더 파일들
└── src/                 # 소스 파일 (.cc)
    ├── DetectorConstruction.cc
    ├── PrimaryGeneratorAction.cc
    └── ...              # 기타 소스 파일들
```
