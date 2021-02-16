const {Concert} = require('../models')

module.exports = {
    async index(req, res) {
        try {
            let concerts = null
            const search = req.query.search
            if (search) {
                concerts = await Concert.findAll({
                    where: {
                        $or: [
                            'title', 'artist', 'date'
                        ].map(key => ({
                            [key]: {
                                $like: `%${search}%`
                            }
                        }))
                    }
                })
            } else {
                concerts = await Concert.findAll({
                    limit: 10
                })
            }
            res.send(concerts)
        } catch (err) {
            res.status(500).send({
                error: 'Ne moze da pronadje pesmu'
            })
        }
    },
    async show(req, res) {
        try {
            const concert = await Concert.findByPk(req.params.concertId)
            res.send(concert)
        } catch (err) {
            res.status(500).send({
                error: 'Ne moze da pronadje pesmu'
            })
        }
    },
    async post(req, res) {
        try {
            // console.log("Usao")
            const concert = await Concert.create(req.body)
            res.send(concert)
        } catch (err) {
            res.status(500).send({
                error: 'Ne moze da se kreira pesma'
            })
        }
    },
    async put(req, res) {
        try {
            // console.log("Usao")
            const concert = await Concert.update(req.body, {
                // update samo onu pesmu ciji id menjamo, song id vucemo iz routes
                where: {
                    id: req.params.concertId
                }
            })
            res.send(this.body)
        } catch (err) {
            res.status(500).send({
                error: 'Ne moze da uradi update'
            })
        }
    },
    async delete(req, res) {
        try {
            // console.log("Usao")
            const concert = await Concert.findByPk(req.params.concertId)
            await  Concert.destroy({
                where: {
                    id: req.params.concertId
                }
            })
            res.send(concert)
        } catch (err) {
            res.status(500).send({
                error: 'Ne moze da uradi delete'
            })
        }
    }
}