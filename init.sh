if [ -n "$INIAD_OPENAI_API_KEY" ]; then
    echo $INIAD_OPENAI_API_KEY > ./key.secret
fi
if [ -n "$SCENEX_API_KEY" ]; then
    echo $SCENEX_API_KEY >  ./scenex.secret
fi

