module.exports = (sequelize, DataTypes) => {
    const UserAttrSchema = sequelize.define("users_test", {
      user_id:{
        type: DataTypes.STRING,
        allowNull: false,
      },
      age: {
        type: DataTypes.INT,
        allowNull: false,
      },
      caa: {
        type: DataTypes.INT,
        allowNull: false,
      },

      chol : {
        type: DataTypes.INT,
        allowNull: false,
      },
      cp: {
        type: DataTypes.INT,
        allowNull: false,
      },
      exng:{
        type: DataTypes.INT,
        allowNull: false,
      },
      
      fbs: {
        type: DataTypes.INT,
        allowNull: false,
      },
      old_peak: {
        type: DataTypes.INT,
        allowNull: false,
      },
      restecg: {
        type: DataTypes.INT,
        allowNull: false,
      },
      output: {
        type: DataTypes.INT,
        allowNull: false,
      },
      slp: {
        type: DataTypes.INT,
        allowNull: false,
      },
      thall: {
        type: DataTypes.INT,
        allowNull: false,
      },
      thalachh: {
        type: DataTypes.INT,
        allowNull: false,
      },
      trtbps: {
        type: DataTypes.INT,
        allowNull: false,
      },
    });
  
    // Users.associate = (models) => {
    //   Users.hasMany(models.Posts, {
    //     onDelete: "cascade",
    //   });
    // };
    return Users;
  };