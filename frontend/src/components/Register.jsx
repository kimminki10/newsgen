import TextBox from "./TextBox";
import "./TextBox.css";
import "./Register.css";

const Register = () => {
  return (
    <div className="register-container">
      <h1>회원가입</h1>
      <strong>
        가입 인증을 위한 이메일을 보내드리오니<br />
        수신 가능한 이메일 주소를 사용해주세요.
      </strong>
      <TextBox label="이메일" type="email" placeholder="Enter email"/>
      <TextBox label="비밀번호" type="password" placeholder="Enter password"/>
      <TextBox label="비밀번호 확인" type="password" placeholder="Repeat password"/>
      <button className="register-btn">가입하기</button>
    </div>
  );
};

export default Register;
