var arrLang = {
    'en': {
        'home': 'Home',
        'tours': 'tours',
        'hotels': 'hotels',
        'services': 'services',
        'blog': 'blog',
        'about': 'about',
        'contact': 'contact',
        'fight': 'fight',
        'car':'car',
        'cruises':'cruises'
    },
    'vn': {
        'home': 'trang chủ',
        'tours': 'du lịch',
        'hotels': 'khách sạn',
        'services': 'dịch vụ',
        'blog': 'blog',
        'about': 'hổ trợ',
        'contact': 'tương tác',
        'fight': 'chuyến đi',
        'car':'xe',
        'cruises':'du lịch'

    }
};
$(function () {
    $('.translate').click(function () {
        var lang = $(this).attr('id');

        $('.lang').each(function (index, element) {
            $(this).text(arrLang[lang][$(this).attr('key')])
        });
    });
});
