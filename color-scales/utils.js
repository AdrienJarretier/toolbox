function parseForm(formSelector) {

    let formData = {};

    let serializedFOrm = $(formSelector).serializeArray();

    // console.log(serializedFOrm);

    for (let field of serializedFOrm) {

        let name = field.name;

        if (name.endsWith('[]')) {

            name = name.slice(0, -2);

            if (!(name in formData)) {

                formData[name] = []

            }
            formData[name].push(field.value);

        }
        else {
            formData[name] = field.value;
        }

    }

    return formData;

}