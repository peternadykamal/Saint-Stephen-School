-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: Dandelion
-- Generation Time: Aug 09, 2023 at 06:48 AM
-- Server version: 8.0.32
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `talmza`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'view profile talmza level', 1, 'view_profile_talmza_level'),
(2, 'change profile talmza level', 1, 'change_profile_talmza_level'),
(3, 'view profile current talmza level', 1, 'view_profile_current_talmza_level_year'),
(4, 'change profile current talmza level', 1, 'change_profile_current_talmza_level_year'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add user', 5, 'add_user'),
(18, 'Can change user', 5, 'change_user'),
(19, 'Can delete user', 5, 'delete_user'),
(20, 'Can view user', 5, 'view_user'),
(21, 'Can add content type', 6, 'add_contenttype'),
(22, 'Can change content type', 6, 'change_contenttype'),
(23, 'Can delete content type', 6, 'delete_contenttype'),
(24, 'Can view content type', 6, 'view_contenttype'),
(25, 'Can add session', 7, 'add_session'),
(26, 'Can change session', 7, 'change_session'),
(27, 'Can delete session', 7, 'delete_session'),
(28, 'Can view session', 7, 'view_session'),
(29, 'Can add address', 8, 'add_address'),
(30, 'Can change address', 8, 'change_address'),
(31, 'Can delete address', 8, 'delete_address'),
(32, 'Can view address', 8, 'view_address'),
(33, 'Can add profile', 1, 'add_profile'),
(34, 'Can change profile', 1, 'change_profile'),
(35, 'Can delete profile', 1, 'delete_profile'),
(36, 'Can view profile', 1, 'view_profile'),
(37, 'Can add user permission tag', 9, 'add_userpermissiontag'),
(38, 'Can change user permission tag', 9, 'change_userpermissiontag'),
(39, 'Can delete user permission tag', 9, 'delete_userpermissiontag'),
(40, 'Can view user permission tag', 9, 'view_userpermissiontag'),
(41, 'Can add talmza level', 10, 'add_talmzalevel'),
(42, 'Can change talmza level', 10, 'change_talmzalevel'),
(43, 'Can delete talmza level', 10, 'delete_talmzalevel'),
(44, 'Can view talmza level', 10, 'view_talmzalevel'),
(45, 'Can add school level', 11, 'add_schoollevel'),
(46, 'Can change school level', 11, 'change_schoollevel'),
(47, 'Can delete school level', 11, 'delete_schoollevel'),
(48, 'Can view school level', 11, 'view_schoollevel'),
(49, 'Can add profile form log', 12, 'add_profileformlog'),
(50, 'Can change profile form log', 12, 'change_profileformlog'),
(51, 'Can delete profile form log', 12, 'delete_profileformlog'),
(52, 'Can view profile form log', 12, 'view_profileformlog'),
(53, 'Can add expenses profile form', 13, 'add_expensesprofileform'),
(54, 'Can change expenses profile form', 13, 'change_expensesprofileform'),
(55, 'Can delete expenses profile form', 13, 'delete_expensesprofileform'),
(56, 'Can view expenses profile form', 13, 'view_expensesprofileform');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$ltjq9S2XdAXWW8ktbgllxR$0Dd/AF7Ws0OLQ/+e0Pdc++34xweXHmNu/OXo4NwV1Jk=', '2023-08-08 14:08:49.745251', 1, '19102929', '', '', 'kamalnadykamal@gmail.com', 1, 1, '2023-08-07 11:38:02.523516'),
(2, 'pbkdf2_sha256$600000$CuWWphygUWudj5mSX0eq2K$5IcZokxQGCQWRtILmxgAYC/cMz9MtEvAAKzHtaMKzsM=', '2023-08-07 16:19:21.588240', 0, 'kamil fayez', '', '', '', 0, 1, '2023-08-07 11:58:35.000000'),
(8, 'pbkdf2_sha256$600000$B3wVCNRy8Tm9rcbWsxzdFt$c+7TF61VOwJuXkUhAcXbBZxcGfahfeI/XJrKQhHze1M=', NULL, 0, '2300008', '', '', '', 0, 1, '2023-08-07 15:03:05.382312'),
(9, 'pbkdf2_sha256$600000$cEUORJK8MhLybDjHnmXFAS$DwkK0rn2QrmqWeu/XnYQhRMNPxDeDw8RkkLxjxBTFng=', NULL, 0, '2300009', '', '', '', 0, 1, '2023-08-07 15:12:26.393189'),
(10, 'pbkdf2_sha256$600000$bOoiQwxQulZNcIowYAUYEX$s8+AAwbV8HbbWGWs6LP3AiKTHgbLTMmhfneJWY6Uzgc=', NULL, 0, '2300010', '', '', '', 0, 1, '2023-08-07 17:33:21.057837');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-08-07 11:40:13.036614', 'a907ef5f-4c11-41bc-9648-355f7d23111d', 'مخدوم', 2, '[{\"changed\": {\"fields\": [\"Tag name\"]}}]', 9, 1),
(2, '2023-08-07 11:42:08.949251', '362754ed-35c2-41e8-8cfc-adc7b1178191', 'الرابع', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(3, '2023-08-07 11:42:20.927405', 'ba6c0d1e-e63d-4d27-a689-c55e65611bd6', 'الثالث', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(4, '2023-08-07 11:42:31.257786', '6b3aa176-2544-403e-8c05-a51fd36a4351', 'الثاني', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(5, '2023-08-07 11:42:39.801347', '74f581f3-cca0-4506-beb3-95a8c938203a', 'الأول', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(6, '2023-08-07 11:42:49.247264', 'd2be3f99-4708-4d55-bee7-49c24094c125', 'تمهيدي', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(7, '2023-08-07 11:42:57.705075', '32e4d997-c061-4018-8a06-02e2cf0aef57', 'اقل من تمهيدي', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 10, 1),
(8, '2023-08-07 11:44:52.097986', '07889dac-ae48-48b8-8d2b-683ee35d8ab2', 'خريج', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(9, '2023-08-07 11:45:03.458201', '0b23ec22-3483-4227-884e-177432bc0b1f', 'جامعة', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(10, '2023-08-07 11:45:12.885257', 'c8fa8e83-73f0-45e5-a820-5e2c7d919239', 'ثانوي', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(11, '2023-08-07 11:45:21.674545', '750700e2-0aa9-462f-83a8-de322f87cc7e', 'الإعدادي', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(12, '2023-08-07 11:45:31.923120', 'af153d90-953b-48e6-b8d8-ffa6e2a32320', 'الابتدائي', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(13, '2023-08-07 11:45:44.195023', 'd0b12a75-71bc-40e4-94ed-9745a604bef3', 'حضانة', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(14, '2023-08-07 11:45:57.050523', '410faf62-e732-4eb4-99bd-0ad117730406', 'اقل من حضانة', 2, '[{\"changed\": {\"fields\": [\"Level name\"]}}]', 11, 1),
(15, '2023-08-07 11:47:15.307053', '34a0f6db-7943-4f4a-87b7-5a96cdd02a3f', '', 1, '[{\"added\": {}}]', 8, 1),
(16, '2023-08-07 11:48:54.087266', '461f8705-d10b-42aa-942d-7a80974506d1', 'كمال نادي كمال 19102929', 1, '[{\"added\": {}}]', 1, 1),
(17, '2023-08-07 11:49:39.487017', '461f8705-d10b-42aa-942d-7a80974506d1', 'كمال نادي كمال 19102929', 2, '[{\"changed\": {\"fields\": [\"User permission tags\"]}}]', 1, 1),
(18, '2023-08-07 11:59:21.206885', '2', 'Kamil_fayez', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 5, 1),
(19, '2023-08-07 12:01:55.045254', 'd2670350-fa09-47f5-b291-38aa52aa7a75', '', 1, '[{\"added\": {}}]', 8, 1),
(20, '2023-08-07 12:02:07.214350', 'dd2e3a99-234b-4a87-92d8-27942d25ce94', 'كاميل فايز Kamil fayez', 1, '[{\"added\": {}}]', 1, 1),
(21, '2023-08-07 12:07:17.961922', '43187974-dc2a-472c-943b-bb6cd8e948f0', 'gr g df gdfg 2300003', 3, '', 1, 1),
(22, '2023-08-07 12:55:13.845085', '4', '2300004', 1, '[{\"added\": {}}]', 5, 1),
(23, '2023-08-07 12:55:19.757486', '4', '2300004', 2, '[]', 5, 1),
(24, '2023-08-07 12:55:41.483538', 'd6850c44-1945-4cf2-ae44-cb4d3147df35', '', 1, '[{\"added\": {}}]', 8, 1),
(25, '2023-08-07 12:55:53.140613', '565512a7-3a03-489a-becc-ffa192da3559', 'bjbk 2300004', 1, '[{\"added\": {}}]', 1, 1),
(26, '2023-08-07 12:55:58.092577', '565512a7-3a03-489a-becc-ffa192da3559', 'bjbk 2300004', 3, '', 1, 1),
(27, '2023-08-07 12:56:07.472498', '13d6d16d-2228-43df-8ffd-2caae9eaa8d9', 'مبنا: yuilgkjygyuk, متفرع من:     hjhjkgk, مجمع سكني:   ghfghfyh', 3, '', 8, 1),
(28, '2023-08-07 13:08:27.385419', 'f902f491-fcaf-4336-b03e-39a784d41aa7', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(30, '2023-08-07 13:09:39.210629', 'a00af02b-e264-499a-bf3b-e8f4b323b3b3', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(31, '2023-08-07 13:10:34.891282', 'ee3f4fb7-1e43-4c33-aa85-6f68c432a444', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(32, '2023-08-07 13:11:04.300314', '8b9b7443-d399-44da-8049-2c87b3c5892f', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(33, '2023-08-07 13:12:31.423026', '9ddf6b68-cded-4aad-92ca-01799f0e6863', 'مبنا: yuilgkjygyuk, متفرع من:     hjhjkgk, مجمع سكني:   ghfghfyh', 3, '', 8, 1),
(34, '2023-08-07 13:12:31.427077', '047194f7-0f75-4494-93f4-21c5f03ecfe9', 'مبنا: yuilgkjygyuk, متفرع من:     hjhjkgk, مجمع سكني:   ghfghfyh', 3, '', 8, 1),
(35, '2023-08-07 13:12:40.366027', '202c05fe-4526-481d-a9d1-34a7aa4d5e71', 'مبنا: yuilgkjygyuk, متفرع من:     hjhjkgk, مجمع سكني:   ghfghfyh', 3, '', 8, 1),
(36, '2023-08-07 13:13:10.784745', 'fdb8494f-3694-42a3-ad8b-7f8a515d817a', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(37, '2023-08-07 13:14:21.638422', '1a020b73-c827-4cb0-adec-f67687ec41a3', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(38, '2023-08-07 13:14:49.285446', '69e9acf7-944f-4ed5-a55c-386b3342c3aa', 'bjbk jikhukjiopjio opopjop kol;\'jkiol', 3, '', 1, 1),
(39, '2023-08-07 17:35:49.226607', '32e4d997-c061-4018-8a06-02e2cf0aef57', 'اقل من تمهيدي', 2, '[{\"changed\": {\"fields\": [\"Number of years\"]}}]', 10, 1),
(40, '2023-08-07 17:36:01.532701', '362754ed-35c2-41e8-8cfc-adc7b1178191', 'الرابع', 2, '[{\"changed\": {\"fields\": [\"Number of years\"]}}]', 10, 1),
(41, '2023-08-07 17:36:10.651349', '362754ed-35c2-41e8-8cfc-adc7b1178191', 'الرابع', 2, '[]', 10, 1),
(42, '2023-08-07 17:37:14.578788', '0a56b406-1c9e-4e6b-bcdb-bf350e946019', 'الخامس', 1, '[{\"added\": {}}]', 10, 1),
(43, '2023-08-07 17:37:18.464786', '362754ed-35c2-41e8-8cfc-adc7b1178191', 'الرابع', 2, '[{\"changed\": {\"fields\": [\"Next level\"]}}]', 10, 1),
(44, '2023-08-07 17:38:43.883197', '74f581f3-cca0-4506-beb3-95a8c938203a', 'الأول', 2, '[{\"changed\": {\"fields\": [\"Number of years\"]}}]', 10, 1),
(45, '2023-08-08 03:42:19.286596', '2af4291b-3b53-4b44-8de1-e288f6754958', 'مبنا: -', 1, '[{\"added\": {}}]', 8, 1),
(46, '2023-08-08 03:42:22.709308', 'dd2e3a99-234b-4a87-92d8-27942d25ce94', 'كاميل فايز', 2, '[{\"changed\": {\"fields\": [\"Address\"]}}]', 1, 1),
(47, '2023-08-08 03:42:53.122216', '34a0f6db-7943-4f4a-87b7-5a96cdd02a3f', 'مبنا: -', 2, '[{\"changed\": {\"fields\": [\"Building\"]}}]', 8, 1),
(48, '2023-08-08 03:42:54.910302', '461f8705-d10b-42aa-942d-7a80974506d1', 'كمال نادي كمال', 2, '[]', 1, 1),
(49, '2023-08-08 03:43:42.822583', 'd2670350-fa09-47f5-b291-38aa52aa7a75', '', 3, '', 8, 1),
(50, '2023-08-08 03:43:42.826577', '89996b24-bc25-4cc4-aaf1-d63349915b67', 'مبنا: 19, شارع: عبدالفتاح كريم', 3, '', 8, 1),
(51, '2023-08-08 03:44:05.095989', '2af4291b-3b53-4b44-8de1-e288f6754958', '', 2, '[{\"changed\": {\"fields\": [\"Building\"]}}]', 8, 1),
(52, '2023-08-08 03:44:07.341786', 'dd2e3a99-234b-4a87-92d8-27942d25ce94', 'كاميل فايز', 2, '[]', 1, 1),
(53, '2023-08-08 03:44:14.495060', '34a0f6db-7943-4f4a-87b7-5a96cdd02a3f', '', 2, '[{\"changed\": {\"fields\": [\"Building\"]}}]', 8, 1),
(54, '2023-08-08 03:44:16.268149', '461f8705-d10b-42aa-942d-7a80974506d1', 'كمال نادي كمال', 2, '[]', 1, 1),
(55, '2023-08-08 03:44:21.590829', '31641ba7-c69a-471b-8632-03051e971b8f', 'جوناثان نشأت عياد شفيق', 2, '[]', 1, 1),
(56, '2023-08-08 03:44:25.004564', '1d1d4571-1067-494e-bf05-282678994402', 'بولا جرجس رمزى يوسف', 2, '[]', 1, 1),
(57, '2023-08-08 03:45:09.004123', 'd3986640-b3f1-4040-bfc6-b6340c9bd2c9', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(58, '2023-08-08 03:45:09.007122', 'd32fb712-c5d1-49ae-809f-1932ff791bdb', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(59, '2023-08-08 03:45:09.010121', 'b547a385-93c9-4761-9166-79d2e9d398f8', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(60, '2023-08-08 03:45:09.013121', '6fe17dc0-3355-4e9b-9ae6-32bbbafde379', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(61, '2023-08-08 03:45:09.016120', '5fad1ac3-7cc4-4ae8-906f-adc9c79e1a51', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(62, '2023-08-08 03:45:09.019120', '18cb2d85-1964-4cc2-a4a0-d65e3927f5e0', '2023 None دفع 20 جنيهات', 3, '', 13, 1),
(63, '2023-08-08 14:09:31.651618', '461f8705-d10b-42aa-942d-7a80974506d1', 'كمال نادي كمال سيدهم', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'auth', 'user'),
(6, 'contenttypes', 'contenttype'),
(7, 'sessions', 'session'),
(8, 'users', 'address'),
(13, 'users', 'expensesprofileform'),
(1, 'users', 'profile'),
(12, 'users', 'profileformlog'),
(11, 'users', 'schoollevel'),
(10, 'users', 'talmzalevel'),
(9, 'users', 'userpermissiontag');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-07 11:37:00.384614'),
(2, 'auth', '0001_initial', '2023-08-07 11:37:00.775612'),
(3, 'admin', '0001_initial', '2023-08-07 11:37:00.884620'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-08-07 11:37:00.897615'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-07 11:37:00.909615'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-08-07 11:37:00.977613'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-08-07 11:37:01.029615'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-08-07 11:37:01.060616'),
(9, 'auth', '0004_alter_user_username_opts', '2023-08-07 11:37:01.073616'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-08-07 11:37:01.124615'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-08-07 11:37:01.129617'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-08-07 11:37:01.140615'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-08-07 11:37:01.192613'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-08-07 11:37:01.241615'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-08-07 11:37:01.269615'),
(16, 'auth', '0011_update_proxy_permissions', '2023-08-07 11:37:01.286616'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-08-07 11:37:01.346615'),
(18, 'sessions', '0001_initial', '2023-08-07 11:37:01.385614'),
(19, 'users', '0001_initial', '2023-08-07 11:37:02.081653'),
(20, 'users', '0002_custom_permissions', '2023-08-07 11:37:02.118615'),
(21, 'users', '0003_remove_schoollevel_prevues_level_and_more', '2023-08-07 11:37:02.664351'),
(22, 'users', '0004_alter_userpermissiontag_child_and_more', '2023-08-07 11:37:02.898400');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('47cjrflgqzua518fqyqi7mqetrwlvlha', '.eJxVjEEOwiAQRe_C2hCEAsWl-56BzDCMVA0kpV0Z765NutDtf-_9l4iwrSVuPS9xJnERZ3H63RDSI9cd0B3qrcnU6rrMKHdFHrTLqVF-Xg_376BAL9-aObBJRG7wCGoIbI1HVCZp45gheHJ-9MDKBDdao3FQGTIRUNZogcX7AwKSOPw:1qSycZ:l585xVcFBc9-hzQOoCEACs1nhqgLeRRJVQOhDDxN1DA', '2023-08-21 11:41:59.602187'),
('v60l7vatav9863h1rg3zoogpdc16jfo7', '.eJxVjEEOwiAQRe_C2hCEAsWle89ABmbGooaa0iYa4921SRe6_e_99xIRlnmIS6MpFhQHsRe73y1BvlJdAV6gnkeZxzpPJclVkRtt8jQi3Y6b-xcYoA3fN3NgkxFd5xOoLrA1PiVlsjaOGYJH53sPrExwvTU6dYqAEAFJJwu8Rhu1VsYa6XEv01MctA1aKSXV-wPHWEHJ:1qT48V:5qwaYBt0wy3f9on03LXqMjSR28_KbrqVA3vVtKNqvis', '2023-09-06 17:35:19.558958'),
('xnmn9k2xpvtb9aku760wtvufq32bh52l', '.eJxVjEEOwiAQRe_C2hCEAsWl-56BzDCMVA0kpV0Z765NutDtf-_9l4iwrSVuPS9xJnERZ3H63RDSI9cd0B3qrcnU6rrMKHdFHrTLqVF-Xg_376BAL9-aObBJRG7wCGoIbI1HVCZp45gheHJ-9MDKBDdao3FQGTIRUNZogcX7AwKSOPw:1qSyZ1:cEHrjMcWyG1HFtA4ddo6mygJo-bWrc_TFiiv1YHjxZE', '2023-08-21 11:38:19.381998');

-- --------------------------------------------------------

--
-- Table structure for table `users_address`
--

CREATE TABLE `users_address` (
  `building` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `street` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `branches_from` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `floor` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apartment_number` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `residential_complexes` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `district` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `additional_details` longtext COLLATE utf8mb4_unicode_ci,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_address`
--

INSERT INTO `users_address` (`building`, `street`, `branches_from`, `floor`, `apartment_number`, `residential_complexes`, `district`, `additional_details`, `id`) VALUES
(NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '2af4291b3b534b448de1e288f6754958'),
(NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '34a0f6db79434f4a87b75a96cdd02a3f'),
('19', 'عبدالفتاح كريم', '', '4', '', '', '', '', 'd1a3a2b7d0ef40ea96a0f8bc08f96a13'),
('101', 'الزمكشرى باكوس ', '', '', '', '', '', 'بجوار ك مارجرجس', 'e457c41cdff5430288a4c1e502f1199d'),
('19', 'عبدالفتاح كريم', '', '4', '', '', '', '', 'fcbaf65ab9e34235b246fbcd3e7c6856');

-- --------------------------------------------------------

--
-- Table structure for table `users_expensesprofileform`
--

CREATE TABLE `users_expensesprofileform` (
  `year` varchar(4) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount_of_money_payed` int NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_for_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_expensesprofileform`
--

INSERT INTO `users_expensesprofileform` (`year`, `amount_of_money_payed`, `id`, `created_for_id`) VALUES
('2023', 5, '0d97b76f2ba74f16948ecd4633b33f0e', 'e08fb7e7cd034b20a265fdc66ac3d14d'),
('2023', 5, '5ac158301af34f5b88ba9b2f83ff0e7d', '1d1d45711067494ebf05282678994402'),
('2023', 65, '8bef9f14ee0d4289b947be699c6c4013', '31641ba7c69a471b863203051e971b8f');

-- --------------------------------------------------------

--
-- Table structure for table `users_profile`
--

CREATE TABLE `users_profile` (
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birthdate` date DEFAULT NULL,
  `current_talmza_level_year` int DEFAULT NULL,
  `current_school_level_year` int DEFAULT NULL,
  `job` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gender` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `father_phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mother_phone_number` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mobile_follow_up_on_WhatsApp` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `confession_father` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `church` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deaconess` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `school_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `talmza_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_profile`
--

INSERT INTO `users_profile` (`name`, `birthdate`, `current_talmza_level_year`, `current_school_level_year`, `job`, `gender`, `phone_number`, `father_phone_number`, `mother_phone_number`, `mobile_follow_up_on_WhatsApp`, `confession_father`, `church`, `deaconess`, `profile_image`, `id`, `address_id`, `school_level_id`, `talmza_level_id`, `user_id`) VALUES
('بولا جرجس رمزى يوسف', '2011-04-06', 1, 1, NULL, 'M', NULL, NULL, '01225083859', '01225083859', 'ابونا كاراس', 'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', 'غير', 'images/profiles/user-default.png', '1d1d45711067494ebf05282678994402', 'd1a3a2b7d0ef40ea96a0f8bc08f96a13', '750700e20aa9462f83a8de322f87cc7e', '32e4d997c06140188a0602e2cf0aef57', 8),
('جوناثان نشأت عياد شفيق', '2019-10-26', 2, 1, NULL, 'M', NULL, NULL, '01273875729', '01273875729', NULL, 'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', 'أغس', 'images/profiles/user-default.png', '31641ba7c69a471b863203051e971b8f', 'e457c41cdff5430288a4c1e502f1199d', '410faf62e7324eb499bd0ad117730406', '32e4d997c06140188a0602e2cf0aef57', 10),
('كمال نادي كمال سيدهم', '2001-09-24', 1, 1, NULL, 'M', NULL, NULL, NULL, NULL, NULL, 'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', 'أغس', 'images/profiles/user-default.png', '461f8705d10b42aa942d7a80974506d1', '34a0f6db79434f4a87b75a96cdd02a3f', '07889dacae4848b88d2b683ee35d8ab2', NULL, 1),
('كاميل فايز', '2001-09-24', 1, 1, NULL, 'M', NULL, NULL, NULL, NULL, NULL, 'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', 'غير', 'images/profiles/user-default.png', 'dd2e3a99234b4a8792d827942d25ce94', '2af4291b3b534b448de1e288f6754958', '07889dacae4848b88d2b683ee35d8ab2', NULL, 2),
('فيلوباتير جرجس رمزي يوسف', '2013-03-09', 2, 5, NULL, 'M', NULL, NULL, '01225083859', '01225083859', 'ابونا كاراس', 'كنيسة السيدة العذراء مريم و الشهيد مارجرجس بغبريال', 'غير', 'images/profiles/user-default.png', 'e08fb7e7cd034b20a265fdc66ac3d14d', 'fcbaf65ab9e34235b246fbcd3e7c6856', 'af153d90953b48e6b8d8ffa6e2a32320', '6b3aa1762544403e8c05a51fd36a4351', 9);

-- --------------------------------------------------------

--
-- Table structure for table `users_profileformlog`
--

CREATE TABLE `users_profileformlog` (
  `log_date` datetime(6) NOT NULL,
  `category_action` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_for_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_profile_user_permission_tags`
--

CREATE TABLE `users_profile_user_permission_tags` (
  `id` bigint NOT NULL,
  `profile_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `userpermissiontag_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_profile_user_permission_tags`
--

INSERT INTO `users_profile_user_permission_tags` (`id`, `profile_id`, `userpermissiontag_id`) VALUES
(8, '1d1d45711067494ebf05282678994402', 'a907ef5f4c1141bc9648355f7d23111d'),
(10, '31641ba7c69a471b863203051e971b8f', 'a907ef5f4c1141bc9648355f7d23111d'),
(2, '461f8705d10b42aa942d7a80974506d1', 'fb109f48aea3495aa9e76cd671dfceb8'),
(3, 'dd2e3a99234b4a8792d827942d25ce94', 'fb109f48aea3495aa9e76cd671dfceb8'),
(9, 'e08fb7e7cd034b20a265fdc66ac3d14d', 'a907ef5f4c1141bc9648355f7d23111d');

-- --------------------------------------------------------

--
-- Table structure for table `users_schoollevel`
--

CREATE TABLE `users_schoollevel` (
  `level_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `level_number` int NOT NULL,
  `number_of_years` int DEFAULT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `previous_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_schoollevel`
--

INSERT INTO `users_schoollevel` (`level_name`, `level_number`, `number_of_years`, `id`, `next_level_id`, `previous_level_id`) VALUES
('خريج', 6, NULL, '07889dacae4848b88d2b683ee35d8ab2', NULL, '07889dacae4848b88d2b683ee35d8ab2'),
('جامعة', 5, NULL, '0b23ec2234834227884e177432bc0b1f', '07889dacae4848b88d2b683ee35d8ab2', 'c8fa8e8373f045e5a8205e2c7d919239'),
('اقل من حضانة', 0, NULL, '410faf62e7324eb499bd0ad117730406', 'd0b12a7571bc40e494ed9745a604bef3', NULL),
('الإعدادي', 3, 3, '750700e20aa9462f83a8de322f87cc7e', 'c8fa8e8373f045e5a8205e2c7d919239', 'af153d90953b48e6b8d8ffa6e2a32320'),
('الابتدائي', 2, 6, 'af153d90953b48e6b8d8ffa6e2a32320', '750700e20aa9462f83a8de322f87cc7e', 'd0b12a7571bc40e494ed9745a604bef3'),
('ثانوي', 4, 3, 'c8fa8e8373f045e5a8205e2c7d919239', '0b23ec2234834227884e177432bc0b1f', '750700e20aa9462f83a8de322f87cc7e'),
('حضانة', 1, 2, 'd0b12a7571bc40e494ed9745a604bef3', 'af153d90953b48e6b8d8ffa6e2a32320', '410faf62e7324eb499bd0ad117730406');

-- --------------------------------------------------------

--
-- Table structure for table `users_talmzalevel`
--

CREATE TABLE `users_talmzalevel` (
  `level_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `level_number` int NOT NULL,
  `number_of_years` int NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `previous_level_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_talmzalevel`
--

INSERT INTO `users_talmzalevel` (`level_name`, `level_number`, `number_of_years`, `id`, `next_level_id`, `previous_level_id`) VALUES
('الخامس', 6, 1, '0a56b4061c9e4e6bbcdbbf350e946019', NULL, '362754ed35c241e88cfcadc7b1178191'),
('اقل من تمهيدي', 0, 2, '32e4d997c06140188a0602e2cf0aef57', 'd2be3f9947084d55bee749c24094c125', NULL),
('الرابع', 5, 1, '362754ed35c241e88cfcadc7b1178191', '0a56b4061c9e4e6bbcdbbf350e946019', 'ba6c0d1ee63d4d27a689c55e65611bd6'),
('الثاني', 3, 2, '6b3aa1762544403e8c05a51fd36a4351', 'ba6c0d1ee63d4d27a689c55e65611bd6', '74f581f3cca04506beb395a8c938203a'),
('الأول', 2, 3, '74f581f3cca04506beb395a8c938203a', '6b3aa1762544403e8c05a51fd36a4351', 'd2be3f9947084d55bee749c24094c125'),
('الثالث', 4, 2, 'ba6c0d1ee63d4d27a689c55e65611bd6', '362754ed35c241e88cfcadc7b1178191', '6b3aa1762544403e8c05a51fd36a4351'),
('تمهيدي', 1, 2, 'd2be3f9947084d55bee749c24094c125', '74f581f3cca04506beb395a8c938203a', '32e4d997c06140188a0602e2cf0aef57');

-- --------------------------------------------------------

--
-- Table structure for table `users_userpermissiontag`
--

CREATE TABLE `users_userpermissiontag` (
  `tag_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `child_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_buttom` tinyint(1) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `parent_id` char(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_userpermissiontag`
--

INSERT INTO `users_userpermissiontag` (`tag_name`, `id`, `child_id`, `is_buttom`, `is_top`, `parent_id`) VALUES
('مخدوم', 'a907ef5f4c1141bc9648355f7d23111d', NULL, 1, 0, NULL),
('admin', 'fb109f48aea3495aa9e76cd671dfceb8', NULL, 0, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_userpermissiontag_permissions`
--

CREATE TABLE `users_userpermissiontag_permissions` (
  `id` bigint NOT NULL,
  `userpermissiontag_id` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_userpermissiontag_permissions`
--

INSERT INTO `users_userpermissiontag_permissions` (`id`, `userpermissiontag_id`, `permission_id`) VALUES
(4, 'a907ef5f4c1141bc9648355f7d23111d', 16),
(6, 'a907ef5f4c1141bc9648355f7d23111d', 28),
(1, 'a907ef5f4c1141bc9648355f7d23111d', 32),
(2, 'a907ef5f4c1141bc9648355f7d23111d', 36),
(3, 'a907ef5f4c1141bc9648355f7d23111d', 40),
(5, 'a907ef5f4c1141bc9648355f7d23111d', 52),
(7, 'fb109f48aea3495aa9e76cd671dfceb8', 13),
(8, 'fb109f48aea3495aa9e76cd671dfceb8', 14),
(9, 'fb109f48aea3495aa9e76cd671dfceb8', 15),
(10, 'fb109f48aea3495aa9e76cd671dfceb8', 16),
(11, 'fb109f48aea3495aa9e76cd671dfceb8', 25),
(12, 'fb109f48aea3495aa9e76cd671dfceb8', 26),
(13, 'fb109f48aea3495aa9e76cd671dfceb8', 27),
(14, 'fb109f48aea3495aa9e76cd671dfceb8', 28),
(15, 'fb109f48aea3495aa9e76cd671dfceb8', 29),
(16, 'fb109f48aea3495aa9e76cd671dfceb8', 30),
(17, 'fb109f48aea3495aa9e76cd671dfceb8', 31),
(18, 'fb109f48aea3495aa9e76cd671dfceb8', 32),
(19, 'fb109f48aea3495aa9e76cd671dfceb8', 41),
(20, 'fb109f48aea3495aa9e76cd671dfceb8', 42),
(21, 'fb109f48aea3495aa9e76cd671dfceb8', 43),
(22, 'fb109f48aea3495aa9e76cd671dfceb8', 44),
(23, 'fb109f48aea3495aa9e76cd671dfceb8', 49),
(24, 'fb109f48aea3495aa9e76cd671dfceb8', 50),
(25, 'fb109f48aea3495aa9e76cd671dfceb8', 51),
(26, 'fb109f48aea3495aa9e76cd671dfceb8', 52),
(27, 'fb109f48aea3495aa9e76cd671dfceb8', 53),
(28, 'fb109f48aea3495aa9e76cd671dfceb8', 54),
(29, 'fb109f48aea3495aa9e76cd671dfceb8', 55),
(30, 'fb109f48aea3495aa9e76cd671dfceb8', 56);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `users_address`
--
ALTER TABLE `users_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_expensesprofileform`
--
ALTER TABLE `users_expensesprofileform`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_expensesprofil_created_for_id_d3b8644f_fk_users_pro` (`created_for_id`);

--
-- Indexes for table `users_profile`
--
ALTER TABLE `users_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `address_id` (`address_id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `users_profile_school_level_id_d8a42a43_fk_users_schoollevel_id` (`school_level_id`),
  ADD KEY `users_profile_talmza_level_id_6eb92185_fk_users_talmzalevel_id` (`talmza_level_id`);

--
-- Indexes for table `users_profileformlog`
--
ALTER TABLE `users_profileformlog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_profileformlog_created_by_id_fd9a3cf0_fk_users_profile_id` (`created_by_id`),
  ADD KEY `users_profileformlog_created_for_id_8b57fbf7_fk_users_profile_id` (`created_for_id`);

--
-- Indexes for table `users_profile_user_permission_tags`
--
ALTER TABLE `users_profile_user_permission_tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_profile_user_permi_profile_id_userpermissio_2061b2a2_uniq` (`profile_id`,`userpermissiontag_id`),
  ADD KEY `users_profile_user_p_userpermissiontag_id_03708b2d_fk_users_use` (`userpermissiontag_id`);

--
-- Indexes for table `users_schoollevel`
--
ALTER TABLE `users_schoollevel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `next_level_id` (`next_level_id`),
  ADD UNIQUE KEY `previous_level_id` (`previous_level_id`);

--
-- Indexes for table `users_talmzalevel`
--
ALTER TABLE `users_talmzalevel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `next_level_id` (`next_level_id`),
  ADD UNIQUE KEY `previous_level_id` (`previous_level_id`);

--
-- Indexes for table `users_userpermissiontag`
--
ALTER TABLE `users_userpermissiontag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tag_name` (`tag_name`),
  ADD KEY `users_userpermissiontag_child_id_f3612627` (`child_id`),
  ADD KEY `users_userpermissiontag_parent_id_ead25f1f` (`parent_id`);

--
-- Indexes for table `users_userpermissiontag_permissions`
--
ALTER TABLE `users_userpermissiontag_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_userpermissiontag__userpermissiontag_id_per_5418b27a_uniq` (`userpermissiontag_id`,`permission_id`),
  ADD KEY `users_userpermission_permission_id_226f4916_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `users_profile_user_permission_tags`
--
ALTER TABLE `users_profile_user_permission_tags`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users_userpermissiontag_permissions`
--
ALTER TABLE `users_userpermissiontag_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_expensesprofileform`
--
ALTER TABLE `users_expensesprofileform`
  ADD CONSTRAINT `users_expensesprofil_created_for_id_d3b8644f_fk_users_pro` FOREIGN KEY (`created_for_id`) REFERENCES `users_profile` (`id`);

--
-- Constraints for table `users_profile`
--
ALTER TABLE `users_profile`
  ADD CONSTRAINT `users_profile_address_id_bb4c9ea7_fk_users_address_id` FOREIGN KEY (`address_id`) REFERENCES `users_address` (`id`),
  ADD CONSTRAINT `users_profile_school_level_id_d8a42a43_fk_users_schoollevel_id` FOREIGN KEY (`school_level_id`) REFERENCES `users_schoollevel` (`id`),
  ADD CONSTRAINT `users_profile_talmza_level_id_6eb92185_fk_users_talmzalevel_id` FOREIGN KEY (`talmza_level_id`) REFERENCES `users_talmzalevel` (`id`),
  ADD CONSTRAINT `users_profile_user_id_2112e78d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_profileformlog`
--
ALTER TABLE `users_profileformlog`
  ADD CONSTRAINT `users_profileformlog_created_by_id_fd9a3cf0_fk_users_profile_id` FOREIGN KEY (`created_by_id`) REFERENCES `users_profile` (`id`),
  ADD CONSTRAINT `users_profileformlog_created_for_id_8b57fbf7_fk_users_profile_id` FOREIGN KEY (`created_for_id`) REFERENCES `users_profile` (`id`);

--
-- Constraints for table `users_profile_user_permission_tags`
--
ALTER TABLE `users_profile_user_permission_tags`
  ADD CONSTRAINT `users_profile_user_p_profile_id_f3aaca1d_fk_users_pro` FOREIGN KEY (`profile_id`) REFERENCES `users_profile` (`id`),
  ADD CONSTRAINT `users_profile_user_p_userpermissiontag_id_03708b2d_fk_users_use` FOREIGN KEY (`userpermissiontag_id`) REFERENCES `users_userpermissiontag` (`id`);

--
-- Constraints for table `users_schoollevel`
--
ALTER TABLE `users_schoollevel`
  ADD CONSTRAINT `users_schoollevel_next_level_id_06148425_fk_users_schoollevel_id` FOREIGN KEY (`next_level_id`) REFERENCES `users_schoollevel` (`id`),
  ADD CONSTRAINT `users_schoollevel_previous_level_id_d9478edc_fk_users_sch` FOREIGN KEY (`previous_level_id`) REFERENCES `users_schoollevel` (`id`);

--
-- Constraints for table `users_talmzalevel`
--
ALTER TABLE `users_talmzalevel`
  ADD CONSTRAINT `users_talmzalevel_next_level_id_8904d407_fk_users_talmzalevel_id` FOREIGN KEY (`next_level_id`) REFERENCES `users_talmzalevel` (`id`),
  ADD CONSTRAINT `users_talmzalevel_previous_level_id_62d68e96_fk_users_tal` FOREIGN KEY (`previous_level_id`) REFERENCES `users_talmzalevel` (`id`);

--
-- Constraints for table `users_userpermissiontag`
--
ALTER TABLE `users_userpermissiontag`
  ADD CONSTRAINT `users_userpermission_child_id_f3612627_fk_users_use` FOREIGN KEY (`child_id`) REFERENCES `users_userpermissiontag` (`id`),
  ADD CONSTRAINT `users_userpermission_parent_id_ead25f1f_fk_users_use` FOREIGN KEY (`parent_id`) REFERENCES `users_userpermissiontag` (`id`);

--
-- Constraints for table `users_userpermissiontag_permissions`
--
ALTER TABLE `users_userpermissiontag_permissions`
  ADD CONSTRAINT `users_userpermission_permission_id_226f4916_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_userpermission_userpermissiontag_id_27f209a8_fk_users_use` FOREIGN KEY (`userpermissiontag_id`) REFERENCES `users_userpermissiontag` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
