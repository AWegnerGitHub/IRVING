export DJANGO_SETTINGS_MODULE=irving_settings.settings
python modelviz.py -a -g -e > dashboard-all.dot
python modelviz.py -a -g -e dashboard > dashboard.dot
dot dashboard-all.dot -Tpng -o dashboard-all.png
dot dashboard.dot -Tpng -o dashboard.png
rm dashboard-all.dot
rm dashboard.dot