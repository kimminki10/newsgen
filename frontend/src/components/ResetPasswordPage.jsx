import React from 'react';
import TextBox from './TextBox';
import './TextBox.css';
import './ResetPasswordPage.css';

const ResetPasswordPage = () => {
    return (
        <div className="reset-container">
            <h1>비밀번호 재설정</h1>
            <strong>
                회원 등록시 사용한 이메일 주소를 입력하십시오.<br />
                비밀번호를 재설정할 수 있는 링크가 포함된 이메일을 보내드립니다.
            </strong>
            <TextBox label="이메일" type="email" placeholder="Enter email"/>
            <button className="reset-btn">비밀번호 복구</button>
        </div>
    );
}

export default ResetPasswordPage;