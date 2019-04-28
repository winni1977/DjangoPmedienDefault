function ini() {
    const specials = document.querySelectorAll('.special_settings');
    Object.keys(specials).map(
        el => specials[el].closest('.info').style.display = 'None'
    );

    const add_another = document.querySelector('input[name="_addanother"]');
    if (add_another) {
        add_another.style.display = 'none';
    }

    const save = document.querySelector('input[name="_save"]');


    const _continue = document.querySelector('input[name="_continue"]');
    if (_continue) {
        _continue.value = 'Zurück zur Übersicht'.toUpperCase();
        _continue.addEventListener(
            'click',
            (ev) => {
                window.location = '/admin/';
                return ev.preventDefault()
            }
        )
    }

    // _continue.style.display = 'none';

}


window.addEventListener('load', () => ini());