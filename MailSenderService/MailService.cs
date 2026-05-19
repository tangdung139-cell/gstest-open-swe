using Microsoft.Extensions.Logging;

namespace MailSenderService;

public class MailService : IMailService
{
    private readonly ILogger<MailService> _logger;

    public MailService(ILogger<MailService> logger)
    {
        _logger = logger;
    }

    public void SendSampleEmail()
    {
        _logger.LogInformation("Preparing to send an email...");
        try
        {
            // Mock SMTP email sending process
            _logger.LogInformation("Mock email sent to recipient@example.com at {Time}" , DateTime.Now);
        }
        catch(Exception ex)
        {
            _logger.LogError("Failed to send email: {Exception}",ex);
        }
    }
 
}