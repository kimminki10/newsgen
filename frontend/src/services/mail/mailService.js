class MailService {
  constructor() {
    // 환경변수에서 백엔드 URL 가져오기
    this.baseUrl = import.meta.env.VITE_API_URL || "http://localhost:3000";
  }

  async sendNewsletter(email, newsData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/mail/send-newsletter`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          data: newsData,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || "Newsletter sending failed");
      }

      return await response.json();
    } catch (error) {
      console.error("Failed to send newsletter:", error);
      throw error;
    }
  }
}

export default new MailService();
