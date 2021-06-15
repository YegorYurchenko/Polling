class FormVote {
    constructor(el) {
        this.form = el;
        this.formInput = this.form.querySelectorAll('.js-vote-input');
        this.formSubmit = this.form.querySelector('.js-vote-submit');

        this.setListeners();
    }

    setListeners() {
        this.formSubmit.addEventListener('click', (e) => {
            if (!this.checkInputs(this.formInput)) {
                e.preventDefault();
            }
        });
    }

    /**
     * Проверяем, есть ли выбранный input
     * @param inputs - текст заголовка
     */
    checkInputs(inputs) {
        let active_input = false;

        inputs.forEach(input => {
            if (input.checked) {
                active_input = true;
            }
        })

        return active_input
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.js-vote-form');
    for (let i = 0; i < items.length; i++) {
        new FormVote(items[i]);
    }
});
