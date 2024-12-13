// 로그인과 회원가입 버튼이 오른쪽 끝에 나타나는 컴포넌트
import React from 'react';
import './TopHeader.css';

const TopHeader = () => {
  return (
    <div className="top-header">
      <button>로그인</button>
      <button>회원가입</button>
    </div>
  );
}

export default TopHeader;