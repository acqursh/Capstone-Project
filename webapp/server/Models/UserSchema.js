//name of table is users in the database

module.exports = (sequelize, DataTypes) => {
    const UserSchema = sequelize.define("users_test", {
      user_id:{
        type: DataTypes.STRING,
        allowNull: false,
      },
      first_name: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      last_name: {
        type: DataTypes.STRING,
        allowNull: false,
      },

      access_token : {
        type: DataTypes.STRING,
        allowNull: false,
      },
      gender: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      weight:{
        type: DataTypes.FLOAT,
        allowNull: false,
      },
      
      age: {
        type: DataTypes.INT,
        allowNull: false,
      },
    });
  
    // Users.associate = (models) => {
    //   Users.hasMany(models.Posts, {
    //     onDelete: "cascade",
    //   });
    // };
    return UserSchema;
  };