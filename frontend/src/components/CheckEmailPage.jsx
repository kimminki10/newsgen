import React from "react";
import "./CheckEmailPage.css";

const CheckEmailPage = () => {
  return (
    <div className="check-email-container">
      <h1>받은 편지함을 확인하세요</h1>
      <strong>
        회원 등록시 사용한 이메일 주소가 있는 경우,
        <br />
        비밀번호를 재설정하는 링크가 포함된 이메일을 보내드립니다.
      </strong>
      <p>스팸메일함을 확인하는 것을 잊지 마세요.</p>
    </div>
  );
};

export default CheckEmailPage;
