# ❌ [에러 메시지 or 문제 상황]

## ⚠️ 발생한 문제
- 어떤 상황에서 발생했는지?

## 🔍 원인 분석
- vscode remote extension 설치
- docker hub 로그인

## ✅ 해결 방법
```bash
# 그룹 만들기
sudo groupadd docker
# 그룹에 현재 유저 넣기
sudo usermod -aG docker $USER
```
## 🔗 참고 자료
- https://docs.docker.com/engine/install/linux-postinstall/
- 