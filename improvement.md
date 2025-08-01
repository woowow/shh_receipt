## 성능 향상 방법

1. 이미지 해상도 조정 (DPI)

- 해상도가 낮을 시 글자가 뭉개짐
- Tesseract가 DPI 정보로 문자 크기를 추정하고 적응형 모델을 조정

Tesseract 권장 DPI : 최소 300이상

2. Grayscale 변환

- 사진을 컬러가 아닌 흑백으로 변환 후, 검은색과 하얀색으로 이진화하여 텍스트를 더욱 명확하게 만듬
- 대부분의 OCR 엔진이 컬러 이미지보다 흑백 이미지를 잘 처리함

3. 사전 사용 중지

- 내부 사전(Dictionary)에 등록된 단어를 사용해 정확도를 높임
- 하지만 영수증의 경우, 특히 우리가 필요한 정보인 상호명(가맹점명)은 사전 등록 단어가 아닐 확률이 높으며, 이외에도 금액은 숫자로 나타내 필요하지 않음
- 인식 오류 방지를 위해 사전을 비활성화

4. 사용자 단어 목록 추가

- 자주 등장하는 특정 단어들을 리스트화하여 활용
- 특정 단어에 대해선 인식률을 높일 수 있음

5. 문자 화이트리스트 설정

- 특정 문자만 인식하게 설정할 수 있음
- 금액을 위한 숫자, 상호명을 위한 한글과 영어를 넣을 시 기존과 동일해 사용 방법 고민해봐야함

### 성능 향상 방법을 더 생각해보고, 학습시켜보는 방향 해보기