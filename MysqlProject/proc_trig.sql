delimiter //
--создание нового мероприятия
create procedure `newEvent` (IN date_start date, IN name varchar(255), IN description varchar(255))
BEGIN
    declare oid int default 0;
    select librarian_id into oid from Schedule where date(start) >= date_start and date(finish) < date_start limit 1;
    CASE
        WHEN oid = 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT CANCELED: no librarians';
        ELSE
            INSERT INTO Event (date_start, organizer_id, name, description)
                values(date_start, oid, name, description);
    END CASE;
END //

--при увольнении библиотекаря нужно почистить расписание
CREATE TRIGGER alter_events_drop_schedule AFTER UPDATE ON Librarian
FOR EACH ROW BEGIN
    IF (DATE(NOW()) >= NEW.work_end_day) THEN
        delete from Schedule where date(start) > date(NOW()) and librarian_id = NEW.id;
	delete from Event where date(date_start) > date(NOW());
    END IF;
END//

delimiter ;
