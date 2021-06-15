class FormCreate {
    constructor(el) {
        this.form = el;
        this.formTitle = this.form.querySelector('.js-form-create-title');
        this.formVariants = this.form.querySelector('.js-form-create-variants');
        this.formSubmit = this.form.querySelector('.js-form-create-submit');

        this.setListeners();
    }

    setListeners() {
        this.formSubmit.addEventListener('click', (e) => {
            if (!this.checkTitle(this.formTitle) || !this.checkVariants(this.formVariants)) {
                e.preventDefault();
            }
        });
    }
    
    /**
     * Проверяем Title на количество символов
     * @param title - текст заголовка
     */
    checkTitle(title) {
        let trim_title = title.value.trim();
        title.value = trim_title;

        if (trim_title.length > 5) {
            return true;
        }

        return false;
    }

    /**
     * Проверяем Variants на количество (не менее 2-х)
     * @param variants - варианты голосования
     */
    checkVariants(variants) {
        let list_variants = variants.value.split('\n');
        list_variants.map(el => el.trim());

        variants.value = list_variants.join('\n');

        if (list_variants.length > 1) {
            return true;
        }

        return false;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.js-form-create');
    for (let i = 0; i < items.length; i++) {
        new FormCreate(items[i]);
    }
});
