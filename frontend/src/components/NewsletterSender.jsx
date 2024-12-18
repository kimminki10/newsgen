import { useState } from "react";
import mailService from "../services/mail/mailService";

const NewsletterSender = ({ newsData }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [email, setEmail] = useState(""); // email state 추가

  const handleSendNewsletter = async () => {
    // email 파라미터 제거
    try {
      setLoading(true);
      setError(null);
      await mailService.sendNewsletter(email, newsData);
      // 성공 메시지 표시
      alert("뉴스레터가 성공적으로 발송되었습니다!");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <input
        type="email"
        placeholder="수신자 이메일"
        value={email} // value 속성 추가
        onChange={(e) => setEmail(e.target.value)}
        className="border p-2 mr-2"
      />
      <button
        onClick={handleSendNewsletter} // email 파라미터 제거
        disabled={loading || !email} // 이메일이 없을 때도 비활성화
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        {loading ? "발송중..." : "뉴스레터 발송"}
      </button>

      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default NewsletterSender;
