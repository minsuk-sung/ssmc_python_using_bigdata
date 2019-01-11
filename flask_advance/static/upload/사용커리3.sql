-- 자료실 테이블 생성
create table tbl_fileBbs 
(
	`id` int(11) not null AUTO_INCREMENT COMMENT '고유번호',
	`title` varchar(32) not null COMMENT '제목',
	`content` TEXT not null COMMENT '내용',
	`author` varchar(50) not null COMMENT '작성자',
	`files` varchar(2048) not null COMMENT '업로드한 파일들',
	`regDate` TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP COMMENT '등록시간',
	primary key (`id`)
)
COMMENT='자료실 테이블'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1
;