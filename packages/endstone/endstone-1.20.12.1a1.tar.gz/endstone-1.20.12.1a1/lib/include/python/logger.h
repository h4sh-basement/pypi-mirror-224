//
// Created by Vincent on 02/08/2023.
//

#ifndef ENDSTONE_LOGGER_H
#define ENDSTONE_LOGGER_H

#include <utility>

#include "bedrock/bedrock_log.h"
#include "endstone.h"

/**
 * @enum LogLevel
 * @brief Specifies the log level.
 */
enum class LogLevel
{
    All = -1,
    Verbose = 1,
    Info = 2,
    Warning = 4,
    Error = 8,
};

class Logger
{
  public:
    explicit Logger(std::string name) : name_(std::move(name)), level_(LogLevel::Info){};
    virtual void log(LogLevel level, const char *format, ...) const;
    void verbose(const char *format, ...) const;
    void info(const char *format, ...) const;
    void warning(const char *format, ...) const;
    void error(const char *format, ...) const;
    void setLevel(LogLevel level);

    static Logger& getLogger(const std::string &name);

    std::string name_;
    LogLevel level_;
};

class PyLogger : public Logger
{
    using Logger::Logger;
    void log(LogLevel level, const char *format, ...) const override;
};

#endif // ENDSTONE_LOGGER_H
