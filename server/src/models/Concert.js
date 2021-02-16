const sq = require('sequelize')

module.exports = (sequelize, DataTypes) => {

    const Concert = sequelize.define('Concert', {
        title: sq.DataTypes.STRING,
        artist: sq.DataTypes.STRING,
        date: sq.DataTypes.INTEGER,
        concertImageUrl: sq.DataTypes.STRING,
    })

    return Concert;
}
