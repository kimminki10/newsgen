import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const EmailVerified = () => {
  return (
    <div className="check-email-container">
      <h1>이메일 인증 완료</h1>
      <strong>이메일 인증이 완료되었습니다.</strong>
    </div>
  );
}

const EmailNotVerified = () => {
  return (
    <div className="check-email-container">
      <h1>이메일 인증 실패</h1>
      <strong>이메일 인증에 실패했습니다.</strong>
    </div>
  );
}

const VerifyEmailPage = () => {
  // 이메일 인증 완료 페이지
  // token 을 받아서 이메일 인증을 완료하는 페이지
  const [isVerified, setIsVerified] = useState(false);
  const {token} = useParams();
  useEffect(() => {
    const verifyEmail = async () => {
      try {
        const response = await axios.get(`/api/user/verify_email/${token}`);
        if (response.status === 200)
          setIsVerified(true);
      } catch (error) {
        console.error(error);
      }
    };
    verifyEmail();
  }, [token]);

  return (
    <div className="check-email-container">
      {isVerified ? <EmailVerified /> : <EmailNotVerified />}
    </div>
  );
};

export default VerifyEmailPage;
