var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index', {
        title: 'Plate-forme Territoire',
        solution: 'solution',
        place: 'Fayol institute',
        logo: 'logosolution.png',
        onglets: {
            'onglet1': 'iconlayer1.png',
            'onglet2': 'iconlayer2.png'
        },
        param_center: '[4.40387,45.4278]',
        param_tabext: '[4.5998,45.3480,4.1655,45.5357]',
        param_baseview: 17,
        param_urlmapserv: 'http://localhost:80/cgi-bin/mapserv?',
        param_mapfile: 'coreMap.map'
    });
});

module.exports = router;
