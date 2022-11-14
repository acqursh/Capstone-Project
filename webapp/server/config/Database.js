import { Sequelize } from "sequelize"
const db = {}
const sequelize = new Sequelize('capstone', 'root', 'kunal1234', {
  host: 'localhost',
  dialect: 'mysql',
  operatorsAliases: false,

  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
})

db.sequelize = sequelize
db.Sequelize = Sequelize

export default db;
