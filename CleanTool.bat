@echo off
set new_file_prefix=cleaned
for %%f in (*) do (
    set new_file_name = %new_file_prefix%_%%f
    echo %%f    %new_file_name%
    python date_trip.py %%f %new_file_name%
)
pause
