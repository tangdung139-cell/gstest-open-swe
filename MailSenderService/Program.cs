// See https://aka.ms/new-console-template for more information
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using System;
using System.IO;
using System.Net;
using System.Net.Mail;

namespace MailSenderService
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var serviceProvider = new ServiceCollection()
                .AddLogging(configure => configure.AddSimpleConsole())
                .AddSingleton<IMailSenderService, SmtpMailSenderService>()
                .AddSingleton<IConfiguration>(provider =>
                {
                    return new ConfigurationBuilder()
                        .SetBasePath(Directory.GetCurrentDirectory())
                        .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                        .Build();
                })
                .BuildServiceProvider();

            var logger = serviceProvider.GetService<ILogger<Program>>();
            logger.LogInformation("Welcome to the MailSenderService!");

            var mailService = serviceProvider.GetService<IMailSenderService>();
            mailService.Send(new MailMessage("from@example.com", "to@example.com", "Test Subject", "Test Body"));
        }
    }

    public interface IMailSenderService
    {
        void Send(MailMessage message);
    }

    public class SmtpMailSenderService : IMailSenderService
    {
        private readonly IConfiguration _configuration;
        private readonly ILogger<SmtpMailSenderService> _logger;

        public SmtpMailSenderService(IConfiguration configuration, ILogger<SmtpMailSenderService> logger)
        {
            _configuration = configuration;
            _logger = logger;
        }

        public void Send(MailMessage message)
        {
            var smtpConfig = _configuration.GetSection("SMTP");
            var smtpClient = new SmtpClient(smtpConfig["Host"])
            {
                Port = int.Parse(smtpConfig["Port"]),
                Credentials = new NetworkCredential(smtpConfig["Username"], smtpConfig["Password"]),
                EnableSsl = true
            };

            try
            {
                smtpClient.Send(message);
                _logger.LogInformation("Email sent successfully.");
            }
            catch (Exception ex)
            {
                _logger.LogError($"Failed to send email: {ex.Message}");
            }
        }
    }
}
