# G4Starter

Geant4 시뮬레이션 프로젝트를 몇 번의 클릭만으로 생성하는 도구입니다.

## 특징

- 설치 불필요한 실행 파일 제공 (예정)
- 화살표 키로 선택하는 직관적인 인터페이스
- 컴파일 가능한 Geant4 C++ 프로젝트 자동 생성
- Windows, macOS, Linux 지원

## 다운로드

[Releases](https://github.com/yourusername/G4Starter/releases) 페이지에서 운영체제에 맞는 파일을 다운로드하세요.

- Windows: `G4Starter.exe`
- macOS: `G4Starter_mac`
- Linux: `G4Starter_linux`

## 사용 방법

1. 다운로드한 파일 실행
2. 화면의 질문에 답변 (화살표 키 + Enter)
3. 생성된 폴더로 이동하여 빌드

```bash
cd YourProject
mkdir build && cd build
cmake ..
make
./YourProject
```

## 개발자용

개발 환경 설정:

```bash
# 저장소 클론
git clone https://github.com/yourusername/G4Starter.git
cd G4Starter

# 가상환경 및 의존성 설치
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 실행
python src/main.py
```

## 라이선스

MIT License
