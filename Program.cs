using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;

public class Program
{
    public static void Main(string[] args)
    {
        var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((context, services) =>
            {
                services.Configure<SmtpSettings>(context.Configuration.GetSection("SmtpSettings"));
                services.AddTransient<IMailSender, MailSender>();
            })
            .ConfigureLogging(logging =>
            {
                logging.ClearProviders();
                logging.AddConsole();
            })
            .Build();

        var mailSender = host.Services.GetRequiredService<IMailSender>();

        // Sample email sending
        mailSender.SendEmail("example@domain.com", "Test Subject", "Test Body");
    }
}

public class SmtpSettings
{
    public string Host { get; set; }
    public int Port { get; set; }
    public string Username { get; set; }
    public string Password { get; set; }
}

public interface IMailSender
{
    void SendEmail(string to, string subject, string body);
}

public class MailSender : IMailSender
{
    private readonly SmtpSettings _smtpSettings;

    public MailSender(IOptions<SmtpSettings> smtpOptions)
    {
        _smtpSettings = smtpOptions.Value;
    }

    public void SendEmail(string to, string subject, string body)
    {
        Console.WriteLine($"Sending email to {to} using SMTP {_smtpSettings.Host}:{_smtpSettings.Port}");
        // Here we would add actual email sending logic.
    }
}
