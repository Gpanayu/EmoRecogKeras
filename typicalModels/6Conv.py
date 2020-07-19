# Import Keras and other essential libs

def CNN6Conv(window):
        
        # create model
        inp = Input((1, window, 12))
        x = Conv2D(32, (5, 5), input_shape=(1, window, 12), activation='relu')(inp)
        x = Conv2D(32, (2, 2), activation='relu')(x)
        x = Conv2D(32, (2, 2), activation='relu')(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
        x = Conv2D(64, (2, 2), activation='relu')(x)
        x = Conv2D(64, (2, 2), activation='relu')(x)
        x = Conv2D(64, (2, 1), activation='relu')(x)
        x = Dropout(0.5)(x)
        x = Flatten()(x)
        out1 = Dense(128, activation='relu')(x)
        out1 = Dropout(0.5)(out1)
        out1 = Dense(2, activation='softmax')(out1)
        out2 = Dense(128, activation='relu')(x)
        out2 = Dropout(0.5)(out2)
        out2 = Dense(2, activation='softmax')(out2)
        model = Model(inp, [out1, out2])
        
        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy', matthews_correlation])
        return model