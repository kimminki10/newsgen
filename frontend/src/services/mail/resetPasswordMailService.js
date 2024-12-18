class ResetPasswordMailService {
  constructor() {
    this.baseUrl = import.meta.env.VITE_API_URL || "http://localhost:3000";
  }

  async sendResetPasswordEmail(email) {
    try {
      const response = await fetch(
        `${this.baseUrl}/api/mail/send-reset-password`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email }),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(
          errorData.message || "Failed to send reset password email"
        );
      }

      return await response.json();
    } catch (error) {
      console.error("Failed to send reset password email:", error);
      throw error;
    }
  }
}

export default new ResetPasswordMailService();
