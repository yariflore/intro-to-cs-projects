INSERT INTO 
	sandbox (int32_value, bool_value, string_value) 
VALUES
	(46290,0, 'Bizcochito!')

UPDATE 
	sandbox 
SET 
	int16_value = 460,
	datetime_value = '2020-12-19 04:45:00'
Where
	id = 5

DELETE FROM sandbox WHERE id = 7
