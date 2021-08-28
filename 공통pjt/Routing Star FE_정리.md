# Routing Star FE_정리

## 전체적인 구조

인스턴스 생성 /  서버 호출 / 등등 구조 정리??

https://devmg.tistory.com/133



## 로그인 페이지

### JWT 인증



### 로고 및 별들 떨어지는 CSS







## 메인 페이지







## 디테일 페이지



## 검색 페이지



## Post 페이지

### draggable

- 참고링크

  https://vuejsexamples.com/vue-drag-and-drop-component-based-on-sortable-js/

- 설치

  ```
  npm i -S vuedraggable
  ```

- vue에서 활용

  ```vue
  import draggable from 'vuedraggable'
    ...
    export default {
       components: {
          draggable,
    },
    ...
  ```

  ``` vue
  <draggable @update="onUpdated">
  </draggable>
  ```

  - update : update event 발생 시, 사용할 수 있는 변수들

  ![image-20210828135159859](Routing Star FE_정리.assets/image-20210828135159859.png)

## Profile 페이지



## 수정 페이지



## error 페이지





## 공통기능

### 헤더



### Nav 



### 좋아요 및 저장 기능 구현



### 라우터 이동 제한



### 페이지 전환 시 animation



### AWS S3에 파일 업로드하기

> Simple Storage Service(S3). 간단한 파일을 보관해주는 서비스를 활용(사실 다양한 서비스를 제공해주기 때문에 Complicated Storage Service라고 볼 수 있습니다.)

- 참고URL

  s3강의영상 : https://www.youtube.com/watch?v=GLM6a6n4U_s&t=1s

  amazon cognito console : https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album.html

  aws-sdk-npm : https://www.npmjs.com/package/aws-sdk

---

2가지 과정을 우선 거쳐야만 합니다.

1. Amazon S3 : 파일을 올리기 위한 웹하드라고 보면 이해하기 쉽습니다.
2. Amazon Cognito : 관리자 외에 다른 사람이 접속을 할 수 있도록 권한을 부여해주는 서비스

#### AWS에서 S3 bucket 만들기

- S3의 구성요소
  - Bucket : 하나의 프로젝트를 Bucket이라고 칭합니다.
  - Folder : 프로젝트 내에서 생기는 폴더
  - Object : Folder안에 저장되는 파일. 파일 또는 파일에 대한 정보를 담은 객체로 보면 됩니다.

- AWS에서 S3 bucket만들기

  ![image-20210803144501460](Routing Star FE_정리.assets/image-20210803144501460.png)

  - 버킷 만들기

  ![image-20210803144527408](Routing Star FE_정리.assets/image-20210803144527408.png)

  - 버킷이름, 물리적인 서버 지역 설정

  ![image-20210803144634273](Routing Star FE_정리.assets/image-20210803144634273.png)

  - 권한설정

  퍼블릭 엑세스 : 파일을 누구나 볼 수 있게 된다는 의미

  1. 공개파일을 업로드하는 것을 차단(체크해제하면 업로드 가능)

  2. 공개파일을 업로드를 하더라도 비공개로 간주되도록 처리(체크 해제하면 공개됨)

  ![image-20210803145017959](Routing Star FE_정리.assets/image-20210803145017959.png)

  - CORS부분 채워주기

    해당 부분을 편집을 눌러서 아래와 같이 채워줍니다.

  ![image-20210827192743154](Routing Star FE_정리.assets/image-20210827192743154.png)

  ```
  [
      {
          "AllowedHeaders": [
              "*"
          ],
          "AllowedMethods": [
              "HEAD",
              "GET",
              "PUT",
              "POST",
              "DELETE"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": [
              "ETag"
          ]
      }
  ]
  ```

  파일을 업로드하게되면 다음과 같은 URL을 만들어주는데 링크를 들어가보면 `AccessDenied`가 됩니다. 즉 접근이 거부되었다는 것. **해당 파일이 외부에서는 접근할 수가 없다는 의미.**

  <img src="../../TIL/공통pjt/프로젝트기록.assets/image-20210803223417732.png" alt="image-20210803223417732" style="zoom:33%;" />

  ![image-20210803223431531](Routing Star FE_정리.assets/image-20210803223431531.png)

  이 문제를 해결하려면 1. 파일을 권한을 모든 사람(퍼블릭 엑세스) 읽기를 허용해주어야만 합니다.

  ![image-20210803223718724](Routing Star FE_정리.assets/image-20210803223718724.png)

  사용자가 직접 페이지에 접속하는것이 아니라 우리가 만든 웹페이지에서 해당 페이지를 사용하는 사용자가 해당 aws에 접근할 수 있는 권한을 부여해주어야만합니다.

#### 자격증명 풀 만들기

- 풀 이름, 인증되지 않은 자격 증명 체크

![image-20210827193905733](Routing Star FE_정리.assets/image-20210827193905733.png)

- 인증되지 않은 역할(Amazon Cognito for unauthenticated users) 편집

  BUCKET_NAME부분을 내가 만든 버킷이름으로 변경해줍니다.

![image-20210827194155327](Routing Star FE_정리.assets/image-20210827194155327.png)

- 버킷이름(albumBucketName), 지역(bucketRegion), 풀ID(IdentityPoolId)를 잘 알고있어야합니다.

  ![image-20210827194552732](Routing Star FE_정리.assets/image-20210827194552732.png)

  ![image-20210827194707473](Routing Star FE_정리.assets/image-20210827194707473.png)

#### Vue에서 활용하기

vue 프로젝트 생성 후

```bash
npm install aws-sdk
```

```vue
<script>
// aws-sdk가져오기
import AWS from 'aws-sdk'

export default {
    data() {
        return {
            albumBucketName: 'routingstar-photo-album',
            bucketRegion: 'ap-northeast-2',
            IdentityPoolId: 'ap-northeast-2:65af3722-b840-4cce-8c5f-956fb7ed025e',
        }
    }
    method: {
    uploadImage() {
        // 지역, ID지정
        AWS.config.update({
    		region: this.bucketRegion,
    		credentials: new AWS.CognitoIdentityCredentials({
        		IdentityPoolId: this.IdentityPoolId,
    		})
		})
        // 버킷 지정
        var s3 = new AWS.S3({
          apiVersion: '2006-03-01',
          params: { Bucket: this.albumBucketName },
        })
        // 받을 이미지 타입, 제목 설정
        s3.upload(
          {
            Key: `thumbnail/${date + image.name}`,
            Body: image,
            ContentType: image.type,
            ACL: 'public-read',
          },
          (err, data) => {
            if (err) {
              console.log(err);
              return alert('There was an error uploading your photo: ', err.message);
            }
            // data : 이미지 업로드 후 받아온 이미지URL
            console.log(data)
          }
        )
    }
}
}

</script>
```





### canvas





### MVC것?





