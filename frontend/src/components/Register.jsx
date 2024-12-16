import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./Register.css";

const TextBox = ({ label, type, placeholder, value, onChange }) => {
  return (
    <div className="text-box">
      <label>{label}</label>
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
};

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (field) => (e) => {
    setFormData({
      ...formData,
      [field]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // 비밀번호 확인 검증
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    // 백엔드로 전송할 데이터 준비 (confirmPassword 제외)
    const registrationData = {
      email: formData.email,
      password: formData.password,
    };

    // 회원가입 로직 구현
    console.log("Registration data:", registrationData);
    // TODO: API 호출 로직 추가
  };

  const handleBackToLogin = () => {
    navigate("/login");
  };

  return (
    <div className="register-container">
      <Link to="/" className="logo">
        Fintrend
      </Link>
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <TextBox
          label="Email"
          type="email"
          placeholder="Enter email"
          value={formData.email}
          onChange={handleChange("email")}
        />
        <TextBox
          label="Password"
          type="password"
          placeholder="Enter password"
          value={formData.password}
          onChange={handleChange("password")}
        />
        <TextBox
          label="Confirm Password"
          type="password"
          placeholder="Confirm password"
          value={formData.confirmPassword}
          onChange={handleChange("confirmPassword")}
        />
        <button type="submit" className="registerBtn">
          Register
        </button>
        <div className="button-container">
          <button type="button" onClick={handleBackToLogin}>
            Back to Login
          </button>
        </div>
      </form>
    </div>
  );
};

export default Register;
