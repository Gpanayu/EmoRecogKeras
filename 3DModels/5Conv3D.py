# Import Keras and other essential libs

def CNN5Conv3D(window):
    
        # create model
        inp = Input((1, window, 3, 5))
        x = Conv3D(32, (9, 2, 3), input_shape=(1, window, 3, 5), activation='relu')(inp)
        x = Conv3D(32, (3, 2, 3), activation='relu')(x)
        x = Conv3D(64, (3, 1, 1), activation='relu')(x)
        x = MaxPooling3D(pool_size=(4, 1, 1))(x)
        x = Conv3D(64, (3, 1, 1), activation='relu')(x)
        x = Conv3D(64, (3, 1, 1), activation='relu')(x)
        x = Dropout(0.5)(x)
        x = Flatten()(x)
        out1 = Dense(128, activation='relu')(x)
        out1 = Dropout(0.5)(out1)
        out1 = Dense(2, activation='softmax')(out1)
        out2 = Dense(128, activation='relu')(x)
        out2 = Dropout(0.5)(out2)
        out2 = Dense(2, activation='softmax')(out2)
        model = Model(inp, [out1, out2])
        
        # compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy', matthews_correlation])
        return model