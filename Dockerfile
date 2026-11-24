FROM alpine:3.24

RUN apk add --no-cache python3 \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup

WORKDIR /myfirstpipeline

COPY --chown=appuser:appgroup saludar.py .

USER appuser

CMD ["python3", "saludar.py"]

