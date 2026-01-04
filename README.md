# G4Starter

> Interactive CLI tool for generating Geant4 simulation projects

[English](#english) | [한국어](#korean)

---

## English

### What is G4Starter?

G4Starter is a command-line tool that generates ready-to-compile Geant4 C++ simulation projects through an interactive interface. No more copying boilerplate code or setting up project structure manually.

### Features

- **No Installation Required**: Single executable file (Windows/macOS/Linux)
- **Interactive CLI**: Select options with arrow keys
- **Flexible Configuration**:
  - Multithreading support (optional)
  - 3 physics list options (QBBC, PhysicsListFactory, Custom modular)
  - ParticleGun or GPS source
  - Optional UserAction classes (Run, Event, Stepping, Tracking, Stacking)
  - SensitiveDetector support
  - Advanced mode: Custom Run class, Hit class
- **Production Ready**: Generated projects compile with Geant4 out of the box

### Installation

#### Option 1: Package Manager (Recommended)

**Windows (WinGet)**
```powershell
winget install evandde.G4Starter
```

**macOS/Linux (Homebrew)**
```bash
brew tap evandde/tap
brew install g4starter
```

#### Option 2: Install Script (macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/evandde/G4Starter/main/install.sh | bash
```

This will download the latest version to `~/.local/bin/g4starter`.

#### Option 3: Manual Download

Download the executable from [Releases](https://github.com/evandde/G4Starter/releases) and run it directly.

> **Note**: Unlike package manager installations (which use `g4starter`), manually downloaded executables retain their original names (`G4Starter.exe`, `G4Starter_mac`, `G4Starter_linux`).

**Using terminal:**

**Windows:**
```powershell
curl -L -o G4Starter.exe https://github.com/evandde/G4Starter/releases/latest/download/G4Starter.exe
.\G4Starter.exe
```

**macOS:**
```bash
curl -L -o G4Starter https://github.com/evandde/G4Starter/releases/latest/download/G4Starter_mac
chmod +x G4Starter
./G4Starter
```

**Linux:**
```bash
curl -L -o G4Starter https://github.com/evandde/G4Starter/releases/latest/download/G4Starter_linux
chmod +x G4Starter
./G4Starter
```

### Quick Start

1. **Run** G4Starter
   ```bash
   # If installed via package manager
   g4starter

   # Or run the downloaded executable directly
   ./G4Starter_mac    # macOS
   ./G4Starter_linux  # Linux
   .\G4Starter.exe    # Windows
   ```

2. **Answer** the interactive questions (use arrow keys to select)

3. **Build** your generated project
   ```bash
   # Windows
   cd YourProject
   mkdir build
   cd build
   cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release
   ninja
   .\YourProject.exe

   # macOS/Linux
   cd YourProject
   mkdir build && cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   make
   ./YourProject
   ```

### Requirements

**To run G4Starter**: None (standalone executable)

**To build generated projects**:
- Geant4 11.0 or later (tested with 11.4)
- CMake 3.16 or later
- C++17 compatible compiler
- **Windows**: Ninja build system recommended
- **macOS/Linux**: Make (usually pre-installed)

### What Gets Generated?

Your project will include:
- `CMakeLists.txt` - Build configuration
- `main.cc` - Application entry point
- `DetectorConstruction` - Geometry setup (World volume)
- `ActionInitialization` - Action registration
- `PrimaryGeneratorAction` - Particle source (Gun or GPS)
- Additional classes based on your configuration:
  - Optional UserAction classes (Run, Event, Stepping, Tracking, Stacking)
  - Optional PhysicsList (for custom modular physics)
  - Optional SensitiveDetector, Run, and Hit classes (advanced mode)
- `vis.mac` - Visualization macro (OpenGL)
- `run.mac` - Run macro (empty template for your commands)

### Troubleshooting

**Issue**: Compilation errors in generated project
**Solution**: Ensure Geant4 environment is set up correctly (`source geant4.sh` on Unix, or use Geant4 command prompt on Windows)

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

### License

MIT License - see [LICENSE](LICENSE) file

---

## Korean

### G4Starter란?

G4Starter는 대화형 인터페이스를 통해 컴파일 가능한 Geant4 C++ 시뮬레이션 프로젝트를 생성하는 명령줄 도구입니다. 더 이상 보일러플레이트 코드를 복사하거나 프로젝트 구조를 수동으로 설정할 필요가 없습니다.

### 주요 기능

- **설치 불필요**: 단일 실행 파일 (Windows/macOS/Linux)
- **대화형 인터페이스**: 화살표 키로 옵션 선택
- **유연한 설정**:
  - 멀티스레딩 지원 (선택 사항)
  - 3가지 물리 리스트 옵션 (QBBC, PhysicsListFactory, Custom)
  - ParticleGun 또는 GPS 소스
  - 선택적 UserAction 클래스들 (Run, Event, Stepping, Tracking, Stacking)
  - SensitiveDetector 지원
  - 고급 모드: Custom Run 클래스, Hit 클래스
- **즉시 사용 가능**: 생성된 프로젝트는 바로 컴파일 가능

### 설치 방법

#### 방법 1: 패키지 매니저 (권장)

**Windows (WinGet)**
```powershell
winget install evandde.G4Starter
```

**macOS/Linux (Homebrew)**
```bash
brew tap evandde/tap
brew install g4starter
```

#### 방법 2: 설치 스크립트 (macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/evandde/G4Starter/main/install.sh | bash
```

최신 버전을 `~/.local/bin/g4starter`에 자동 설치합니다.

#### 방법 3: 수동 다운로드

[Releases](https://github.com/evandde/G4Starter/releases)에서 실행 파일을 다운로드하여 직접 실행하세요.

> **참고**: 패키지 매니저 설치(`g4starter` 명령어)와 달리, 수동 다운로드한 실행 파일은 원본 이름(`G4Starter.exe`, `G4Starter_mac`, `G4Starter_linux`)을 유지합니다.

**터미널 사용:**

**Windows:**
```powershell
curl -L -o G4Starter.exe https://github.com/evandde/G4Starter/releases/latest/download/G4Starter.exe
.\G4Starter.exe
```

**macOS:**
```bash
curl -L -o G4Starter https://github.com/evandde/G4Starter/releases/latest/download/G4Starter_mac
chmod +x G4Starter
./G4Starter
```

**Linux:**
```bash
curl -L -o G4Starter https://github.com/evandde/G4Starter/releases/latest/download/G4Starter_linux
chmod +x G4Starter
./G4Starter
```

### 사용 방법

1. **G4Starter 실행**
   ```bash
   # 패키지 매니저로 설치한 경우
   g4starter

   # 또는 다운로드한 실행 파일 직접 실행
   ./G4Starter_mac    # macOS
   ./G4Starter_linux  # Linux
   .\G4Starter.exe    # Windows
   ```

2. **질문에 답변** (화살표 키로 선택)

3. **프로젝트 빌드**
   ```bash
   # Windows
   cd YourProject
   mkdir build
   cd build
   cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release
   ninja
   .\YourProject.exe

   # macOS/Linux
   cd YourProject
   mkdir build && cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   make
   ./YourProject
   ```

### 요구 사항

**G4Starter 실행**: 없음 (독립 실행 파일)

**생성된 프로젝트 빌드**:
- Geant4 11.0 이상 (11.4에서 테스트됨)
- CMake 3.16 이상
- C++17 호환 컴파일러
- **Windows**: Ninja 빌드 시스템 권장
- **macOS/Linux**: Make (보통 기본 설치됨)

### 생성되는 파일

프로젝트에 포함되는 파일:
- `CMakeLists.txt` - 빌드 설정
- `main.cc` - 애플리케이션 진입점
- `DetectorConstruction` - 지오메트리 설정 (World volume)
- `ActionInitialization` - 액션 등록
- `PrimaryGeneratorAction` - 입자 소스 (Gun 또는 GPS)
- 설정에 따른 추가 클래스:
  - 선택적 UserAction 클래스들 (Run, Event, Stepping, Tracking, Stacking)
  - 선택적 PhysicsList (커스텀 모듈식 물리)
  - 선택적 SensitiveDetector, Run, Hit 클래스 (고급 모드)
- `vis.mac` - 시각화 매크로 (OpenGL)
- `run.mac` - 실행 매크로 (빈 템플릿)

### 문제 해결

**문제**: 생성된 프로젝트 컴파일 오류
**해결**: Geant4 환경이 올바르게 설정되었는지 확인 (Unix: `source geant4.sh`, Windows: Geant4 명령 프롬프트 사용)

### 기여하기

개발 환경 설정 및 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참조하세요.

### 라이선스

MIT License - [LICENSE](LICENSE) 파일 참조
