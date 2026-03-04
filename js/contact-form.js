// Contact Form — mailto with confirmation feedback
function sendContactEmail(e) {
    e.preventDefault();
    var form = e.target;
    var name = (form.querySelector('input[name="name"]') || {}).value || '';
    var email = (form.querySelector('input[name="email"]') || {}).value || '';
    var company = (form.querySelector('input[name="company"]') || {}).value || '';
    var details = (form.querySelector('textarea[name="details"]') || {}).value || '';

    name = name.trim();
    email = email.trim();
    company = company.trim();
    details = details.trim();

    var isEN = window.location.search.indexOf('lang=en') !== -1;

    var subject = encodeURIComponent(
        isEN
            ? 'Contact request from ' + name + (company ? ' - ' + company : '')
            : 'Contactverzoek van ' + name + (company ? ' - ' + company : '')
    );
    var body = encodeURIComponent(
        isEN
            ? 'Hello,\n\nMy name is ' + name + (company ? ' from ' + company : '') + ' (' + email + ').\n\n' + details + '\n\nKind regards,\n' + name
            : 'Hallo,\n\nIk ben ' + name + (company ? ' van ' + company : '') + ' (' + email + ').\n\n' + details + '\n\nMet vriendelijke groet,\n' + name
    );

    window.location.href = 'mailto:klantcontact@interactivemove.nl?subject=' + subject + '&body=' + body;

    var btn = form.querySelector('button[type="submit"]');
    if (btn) {
        var original = btn.innerHTML;
        btn.innerHTML = isEN ? 'Email client opened' : 'E-mail client geopend';
        btn.style.background = '#28a745';
        btn.style.color = '#fff';
        setTimeout(function() { btn.innerHTML = original; btn.style.background = ''; btn.style.color = ''; }, 3000);
    }
}
