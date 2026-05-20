using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using System;
using System.Net;
using System.Net.Mail;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var host = CreateHostBuilder(args).Build();
        var mailService = host.Services.GetRequiredService<IMailSenderService>();

        // Sample call to send email
        await mailService.SendEmailAsync("test@example.com", "Test Subject", "Test Body");
    }

    static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureAppConfiguration((hostingContext, config) =>
            {
                config.AddJsonFile("appsettings.json", optional: true, reloadOnChange: true);
            })
            .ConfigureServices((hostContext, services) =>
            {
                services.AddTransient<IMailSenderService, MailSenderService>();
            })
            .ConfigureLogging(logging =>
            {
                logging.ClearProviders();
                logging.AddConsole();
            });
}

public interface IMailSenderService
{
    Task SendEmailAsync(string to, string subject, string body);
}

public class MailSenderService : IMailSenderService
{
    private readonly IConfiguration _configuration;
    private readonly ILogger<MailSenderService> _logger;

    public MailSenderService(IConfiguration configuration, ILogger<MailSenderService> logger)
    {
        _configuration = configuration;
        _logger = logger;
    }

    public async Task SendEmailAsync(string to, string subject, string body)
    {
        var smtpSettings = _configuration.GetSection("Smtp").Get<SmtpSettings>();

        try
        {
            var smtpClient = new SmtpClient(smtpSettings.Host)
            {
                Port = smtpSettings.Port,
                Credentials = new NetworkCredential(smtpSettings.Username, smtpSettings.Password),
                EnableSsl = smtpSettings.EnableSsl
            };

            var mailMessage = new MailMessage
            {
                From = new MailAddress(smtpSettings.Username),
                Subject = subject,
                Body = body,
                IsBodyHtml = false
            };

            mailMessage.To.Add(to);

            await smtpClient.SendMailAsync(mailMessage);

            _logger.LogInformation($"Email sent to {to}");
        }
        catch (Exception ex)
        {
            _logger.LogError($"Failed to send email: {ex.Message}");
            throw;
        }
    }
}

public class SmtpSettings
{
    public string Host { get; set; }
    public int Port { get; set; }
    public bool EnableSsl { get; set; }
    public string Username { get; set; }
    public string Password { get; set; }
}
