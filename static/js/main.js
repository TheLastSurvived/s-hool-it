
if (document.querySelector('#div_id_interests')) {
    const interests = document.querySelector('#div_id_interests').querySelector('.form-control-label');
    interests.innerHTML = 'Интересы';
}

if (document.querySelector('#div_id_name')) {
    const name = document.querySelector('#div_id_name').querySelector('.form-control-label');
    name.innerHTML = 'Название'; 
}

if (document.querySelector('#div_id_subject')) {
    const subject = document.querySelector('#div_id_subject').querySelector('.form-control-label');
    subject.innerHTML = 'Тема';  
}

if (document.querySelector('#div_id_text')) {
    const question = document.querySelector('#div_id_text').querySelector('.form-control-label');

    question.innerHTML = 'Вопрос:';  
}

if (document.querySelector('#div_id_answer')) {
    const an = document.querySelector('#div_id_answer').querySelector('.form-control-label');
   
    an.innerHTML = 'Ответы:';  
}






