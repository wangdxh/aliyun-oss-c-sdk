#include "oss_define.h"

const char OSS_CANNONICALIZED_HEADER_PREFIX[] = "x-amz-";
const char OSS_CANNONICALIZED_HEADER_DATE[] = "x-amz-date";
const char OSS_CANNONICALIZED_HEADER_ACL[] = "x-amz-acl";
const char OSS_CANNONICALIZED_HEADER_STORAGE_CLASS[] = "StorageClass";
const char OSS_CANNONICALIZED_HEADER_COPY_SOURCE[] = "x-amz-copy-source";

const char OSS_CANNONICALIZED_HEADER_REGION[] = "x-amz-bucket-region";

const char OSS_CONTENT_MD5[] = "Content-MD5";
const char OSS_CONTENT_TYPE[] = "Content-Type";
const char OSS_CONTENT_LENGTH[] = "Content-Length";
const char OSS_DATE[] = "Date";
const char OSS_AUTHORIZATION[] = "Authorization";
const char OSS_ACCESSKEYID[] = "OSSAccessKeyId";
const char OSS_EXPECT[] = "Expect";
const char OSS_EXPIRES[] = "Expires";
const char OSS_SIGNATURE[] = "Signature";
const char OSS_ACL[] = "acl";
const char OSS_LOCATION[] = "location";
const char OSS_BUCKETINFO[] = "bucketInfo";
const char OSS_BUCKETSTAT[] = "stat";
const char OSS_RESTORE[] = "restore";
const char OSS_SYMLINK[] = "symlink";
const char OSS_QOS[] = "qos";
const char OSS_PREFIX[] = "prefix";
const char OSS_DELIMITER[] = "delimiter";
const char OSS_MARKER[] = "marker";
const char OSS_MAX_KEYS[] = "max-keys";
const char OSS_UPLOADS[] = "uploads";
const char OSS_UPLOAD_ID[] = "uploadId";
const char OSS_MAX_PARTS[] = "max-parts";
const char OSS_PART_NUMBER_MARKER[] = "part-number-marker";
const char OSS_KEY_MARKER[] = "key-marker";
const char OSS_UPLOAD_ID_MARKER[] = "upload-id-marker";
const char OSS_MAX_UPLOADS[] = "max-uploads";
const char OSS_PARTNUMBER[] = "partNumber";
const char OSS_APPEND[] = "append";
const char OSS_POSITION[] = "position";
const char OSS_MULTIPART_CONTENT_TYPE[] = "application/x-www-form-urlencoded";
const char OSS_COPY_SOURCE[] = "x-amz-copy-source";
const char OSS_COPY_SOURCE_RANGE[] = "x-amz-copy-source-range";
const char OSS_SECURITY_TOKEN[] = "security-token";
const char OSS_STS_SECURITY_TOKEN[] = "x-amz-security-token";

// next two from https://github.com/ceph/ceph/pull/22755
const char OSS_OBJECT_TYPE[] = "x-amz-object-type";  
const char OSS_NEXT_APPEND_POSITION[] = "x-rgw-next-append-position";

// not find in amz  为了签名通过，修改成amz
const char OSS_CANNONICALIZED_HEADER_SYMLINK[] = "x-amz-symlink-target";
const char OSS_CANNONICALIZED_HEADER_OBJECT_ACL[] = "x-amz-object-acl";
const char OSS_HASH_CRC64_ECMA[] = "x-amz-hash-crc64ecma";
const char OSS_CALLBACK[] = "x-amz-callback";
const char OSS_CALLBACK_VAR[] = "x-amz-callback-var";
const char OSS_PROCESS[] = "x-amz-process";
const char OSS_SELECT_OBJECT_OUTPUT_RAW[] = "x-amz-select-output-raw";
const char OSS_SIGN_ORIGIN_ONLY[] = "x-amz-sign-origin-only";

const char OSS_LIFECYCLE[] = "lifecycle";
const char OSS_REFERER[] = "referer";
const char OSS_CORS[] = "cors";
const char OSS_WEBSITE[] = "website";
const char OSS_LOGGING[] = "logging";
const char OSS_DELETE[] = "delete";
const char OSS_YES[] = "yes";
const char OSS_OBJECT_TYPE_NORMAL[] = "Normal";
const char OSS_OBJECT_TYPE_APPENDABLE[] = "Appendable";
const char OSS_LIVE_CHANNEL[] = "live";
const char OSS_LIVE_CHANNEL_STATUS[] = "status";
const char OSS_COMP[] = "comp";
const char OSS_LIVE_CHANNEL_STAT[] = "stat";
const char OSS_LIVE_CHANNEL_HISTORY[] = "history";
const char OSS_LIVE_CHANNEL_VOD[] = "vod";
const char OSS_LIVE_CHANNEL_START_TIME[] = "startTime";
const char OSS_LIVE_CHANNEL_END_TIME[] = "endTime";
const char OSS_PLAY_LIST_NAME[] = "playlistName";
const char LIVE_CHANNEL_STATUS_DISABLED[] = "disabled";
const char LIVE_CHANNEL_STATUS_ENABLED[] = "enabled";
const char LIVE_CHANNEL_STATUS_IDLE[] = "idle";
const char LIVE_CHANNEL_STATUS_LIVE[] = "live";
const char LIVE_CHANNEL_DEFAULT_TYPE[] = "HLS";
const char LIVE_CHANNEL_DEFAULT_PLAYLIST[] = "playlist.m3u8";
const int  LIVE_CHANNEL_DEFAULT_FRAG_DURATION = 5;
const int  LIVE_CHANNEL_DEFAULT_FRAG_COUNT = 3;
const int OSS_MAX_PART_NUM = 10000;
const int OSS_PER_RET_NUM = 1000;
const int MAX_SUFFIX_LEN = 1024;
const char OSS_OBJECT_META[] = "objectMeta";

const char OSS_TAGGING[] = "tagging";


