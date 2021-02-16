const AuthenticationController = require('./controllers/AuthenticationController')
const AuthenticationControllerPolicy = require('./validacija/AuthenticationControllerPolicy')
const SongsController = require('./controllers/SongsController')
const ConcertsController = require('./controllers/ConcertsController')
module.exports = (app) => {
    app.post('/register',
        AuthenticationControllerPolicy.register,
        AuthenticationController.register)

    app.post('/login',
        AuthenticationController.login)

    app.get('/songs',
        SongsController.index)

    app.post('/songs',
        SongsController.post)

    app.get('/songs/:songId',
        SongsController.show)

    app.put('/songs/:songId',
        SongsController.put)

    app.delete('/songs/:songId',
        SongsController.delete)

    app.get('/concerts',
        ConcertsController.index)

    app.post('/concerts',
        ConcertsController.post)

    app.get('/concerts/:concertId',
        ConcertsController.show)

    app.put('/concerts/:concertId',
        ConcertsController.put)

    app.delete('/concerts/:concertnpm Id',
        ConcertsController.delete)
}
