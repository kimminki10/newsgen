import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import "./NewPasswordPage.css";

const NewPasswordPage = () => {
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const { token } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const verifyToken = async () => {
      try {
        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/api/auth/verify-reset-token`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ token }),
          }
        );

        if (!response.ok) {
          throw new Error("Invalid or expired token");
        }
      } catch (err) {
        setError(
          "유효하지 않거나 만료된 링크입니다. 비밀번호 재설정을 다시 요청해주세요."
        );
      }
    };

    verifyToken();
  }, [token]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 비밀번호 유효성 검사
    if (password.length < 8) {
      setError("비밀번호는 8자 이상이어야 합니다.");
      return;
    }

    if (password !== confirmPassword) {
      setError("비밀번호가 일치하지 않습니다.");
      return;
    }

    try {
      setLoading(true);
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/auth/reset-password`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            token,
            newPassword: password,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to reset password");
      }

      alert("비밀번호가 성공적으로 재설정되었습니다.");
      navigate("/login");
    } catch (err) {
      setError("비밀번호 재설정에 실패했습니다. 다시 시도해주세요.");
    } finally {
      setLoading(false);
    }
  };

  // 버튼 활성화 여부를 결정하는 조건
  const isSubmitDisabled = () => {
    return loading || !password || !confirmPassword || password.length < 8;
  };

  return (
    <form onSubmit={handleSubmit} className="new-password-container">
      <h1>비밀번호 재설정</h1>
      <div className="password-fields">
        <TextBox
          label="새로운 비밀번호"
          type="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
            setError(""); // 입력 시 에러 메시지 초기화
          }}
          placeholder="8자 이상 입력해주세요"
          required
        />
        <TextBox
          label="새로운 비밀번호 확인"
          type="password"
          value={confirmPassword}
          onChange={(e) => {
            setConfirmPassword(e.target.value);
            setError(""); // 입력 시 에러 메시지 초기화
          }}
          placeholder="비밀번호를 다시 입력해주세요"
          required
        />
      </div>
      {error && <p className="error-message">{error}</p>}
      <button
        type="submit"
        className="submit-btn"
        disabled={isSubmitDisabled()}
      >
        {loading ? "처리중..." : "재설정하기"}
      </button>
    </form>
  );
};

export default NewPasswordPage;
