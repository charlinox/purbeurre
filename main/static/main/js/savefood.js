window.onload = function() {
    main()
    notMatch() // see the notmatch.js file for more details
};

function main() {

    // ************* see the secureajax.js file for more details ******************************
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // ****************************************************************************************

    var btn = document.getElementsByClassName('btn-save-food');
    var userSession = document.getElementById('user_session').textContent;
    var titleModalBox = document.getElementById('titleBox');
    var bodyModalBox = document.getElementById('bodyBox');

    if (userSession === 'True') {

        for (let i = 0; i < btn.length; i++) {

            btn[i].addEventListener('click', function (event) {
                var nameFood = btn[i].dataset.productName;

                $.ajax({
                    url: '/favorites/save_food/',
                    type: 'POST',
                    dataType: 'json',
                    data: {'substitute-id': btn[i].dataset.substituteId, 'product-id': btn[i].dataset.productId},
                    success: function (data) {
                        titleModalBox.textContent = 'Sauvegarde...';
                        bodyModalBox.textContent = 'Le produit ' + nameFood + ' a bien été ajouté à vos favoris';
                        $('#modalBox').modal();
                    },
                    error: function (error) {
                        titleModalBox.textContent = 'Erreur';
                        bodyModalBox.textContent = 'Le produit ' + nameFood + " n'a pas été ajouté à vos favoris.\nUne erreur c'est produite.";
                        $('#modalBox').modal();
                    }
                })
            });
        }
    }else {

        for (let i = 0; i < btn.length; i++) {

            btn[i].addEventListener('click', function (event) {
                titleModalBox.textContent = 'Notification';
                bodyModalBox.classList.add('text-danger');
                bodyModalBox.textContent = "Vous devez vous connectez pour sauvegarder l'aliment";
                $('#modalBox').modal();
            });
        }
    }
}