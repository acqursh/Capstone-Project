import { Sequelize } from 'sequelize'
import db from "../config/Database.js"

const Users = db.sequelize.define(
  'user',
  {
    email_id: {
      type: Sequelize.STRING,
      primaryKey: true
    },
    first_name: {
      type: Sequelize.STRING
    },
    last_name: {
      type: Sequelize.STRING
    },
    password: {
      type: Sequelize.STRING
    },
    gender: {
      type: Sequelize.STRING
    },
    weight: {
      type: Sequelize.INTEGER
    },
    age: {
      type: Sequelize.INTEGER
    },
    user_id: {
      type: Sequelize.INTEGER,
      autoIncrement: true
    },
  },
  {
    timestamps: false
  }
)
export default Users;