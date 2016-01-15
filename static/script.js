var submit = $('#submit'), sentence_box = $("input[name=sentence]");

submit.click( function(e) {
    e.preventDefault();

    sentence = sentence_box.val();

    if (sentence) {
        sentence = encodeURIComponent(sentence);

        $.getJSON('/predict/'+sentence).done( function(json) {
            $('#attitude h3').text( json.attitude.category );
            $('#intensity h3').text( json.intensity.category );
            $('#polarity h3').text( json.polarity.category );
            $('#expression h3').text( json.expression.category );

            switch (json.intensity.category) {
                case 'low':
                    c = 'dark-blue';
                    break;
                case 'low-medium':
                    c = 'indigo';
                    break;
                case 'medium':
                    c = 'yellow';
                    break;
                case 'medium-high':
                    c = 'amber';
                    break;
                case 'high':
                    c = 'orange';
                    break;
                case 'high-extreme':
                    c = 'red';
                    break;
                case 'extreme':
                    c = 'dark-red';
                    break;
                default:
                    c = 'grey';
            };
            $('#intensity').removeClass().addClass('section').addClass(c);

            if (json.polarity.category.indexOf('positive') > -1) c = 'green';
            else if (json.polarity.category.indexOf('negative') > -1) c = 'dark-red';
            else if (json.polarity.category.indexOf('neutral') > -1) c = 'dark-blue';
            else if (json.polarity.category.indexOf('both') > -1) c = 'yellow';
            else c = 'grey'
            $('#polarity').removeClass().addClass('section').addClass(c);

            if (json.attitude.category.indexOf('pos') > -1) c = 'green';
            else if (json.attitude.category.indexOf('neg') > -1) c = 'dark-red';
            else if (json.attitude.category.indexOf('other-attitude') > -1) c = 'dark-blue';
            else if (json.attitude.category.indexOf('speculation') > -1) c = 'indigo';
            else if (json.attitude.category.indexOf('both') > -1) c = 'yellow';
            else c = 'grey'
            $('#attitude').removeClass().addClass('section').addClass(c);

            switch (json.expression.category) {
                case 'low':
                    c = 'dark-blue';
                    break;
                case 'medium':
                    c = 'yellow';
                    break;
                case 'high':
                    c = 'red';
                    break;
                case 'extreme':
                    c = 'dark-red';
                    break;
                default:
                    c = 'grey'
            };
            $('#expression').removeClass().addClass('section').addClass(c);
        });
    }
    return;
});

$('.info').click( function(e) {
    $('#'+$(this).attr('metric')).slideToggle()
})
