#!/usr/bin/env bash
chmod +x probe.sh
pytest Notification_service_postman.py --html=report_Notification_service.html --self-contained-html
